import csv
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# ---------- Logging setup ----------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)
logger = logging.getLogger("upload_service")

# ---------- DB setup ----------

DB_PATH = "sqlite:///./upload_demo.db"
engine = create_engine(DB_PATH, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    status = Column(String, default="pending")  # pending | processing | done | failed
    created_at = Column(DateTime, default=datetime.utcnow)
    finished_at = Column(DateTime, nullable=True)
    error_message = Column(String, nullable=True)

    records = relationship("Record", back_populates="job")


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)
    col1 = Column(String, nullable=True)
    col2 = Column(String, nullable=True)
    col3 = Column(String, nullable=True)

    job = relationship("Job", back_populates="records")


Base.metadata.create_all(bind=engine)

# ---------- Pydantic schemas ----------


class JobOut(BaseModel):
    id: int
    filename: str
    status: str
    created_at: datetime
    finished_at: Optional[datetime]
    error_message: Optional[str]
    record_count: int

    # Pydantic v2 config: replacement for orm_mode = True
    model_config = ConfigDict(from_attributes=True)


# ---------- FastAPI app ----------

app = FastAPI(title="Upload Demo")


def get_db():
    """Simple dependency-style helper to get a DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Background processing ----------


def process_csv_file(job_id: int, file_path: Path):
    """Runs in the background. Parse CSV and store rows in DB."""
    logger.info("Starting background processing for job_id=%s", job_id)
    db = SessionLocal()
    try:
        job: Job = db.get(Job, job_id)
        if job is None:
            logger.error("Job %s not found in DB", job_id)
            return

        job.status = "processing"
        db.commit()

        inserted = 0
        with file_path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            _header = next(reader, None)  # skip header if present

            for row in reader:
                col1 = row[0] if len(row) > 0 else None
                col2 = row[1] if len(row) > 1 else None
                col3 = row[2] if len(row) > 2 else None

                rec = Record(job_id=job_id, col1=col1, col2=col2, col3=col3)
                db.add(rec)
                inserted += 1

            db.commit()

        job.status = "done"
        job.finished_at = datetime.utcnow()
        db.commit()

        logger.info(
            "Finished processing job_id=%s, inserted=%s rows", job_id, inserted
        )
    except Exception as exc:  # noqa: BLE001
        logger.exception("Error while processing job_id=%s", job_id)
        job = db.get(Job, job_id)
        if job:
            job.status = "failed"
            job.error_message = str(exc)
            job.finished_at = datetime.utcnow()
            db.commit()
    finally:
        db.close()
        try:
            file_path.unlink(missing_ok=True)
        except Exception:
            logger.warning("Could not delete temp file %s", file_path)


# ---------- Endpoints ----------


@app.post("/upload", response_class=JSONResponse)
async def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
):
    # Basic validation
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Only .csv files are supported in this example",
        )

    # Save to a temporary location
    temp_dir = Path("tmp")
    temp_dir.mkdir(exist_ok=True)
    temp_path = temp_dir / f"{datetime.utcnow().timestamp()}_{file.filename}"

    contents = await file.read()
    temp_path.write_bytes(contents)

    # Create DB job entry
    db = SessionLocal()
    try:
        job = Job(filename=file.filename, status="pending")
        db.add(job)
        db.commit()
        db.refresh(job)

        logger.info("Created job_id=%s for file=%s", job.id, file.filename)

        # Schedule background processing
        background_tasks.add_task(process_csv_file, job.id, temp_path)

        return {"job_id": job.id, "status": job.status}
    finally:
        db.close()


@app.get("/jobs/{job_id}", response_model=JobOut)
def get_job(job_id: int):
    db = SessionLocal()
    try:
        job = db.get(Job, job_id)
        if job is None:
            raise HTTPException(status_code=404, detail="Job not found")

        record_count = db.query(Record).filter(Record.job_id == job_id).count()

        return JobOut(
            id=job.id,
            filename=job.filename,
            status=job.status,
            created_at=job.created_at,
            finished_at=job.finished_at,
            error_message=job.error_message,
            record_count=record_count,
        )
    finally:
        db.close()


@app.get("/health")
def healthcheck():
    return {"status": "ok"}
