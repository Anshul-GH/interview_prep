from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import time
import re

app = FastAPI(title="Mini RAG Prototype")

DOCS_DIR = Path("docs")
CHUNKS = []

class AskRequest(BaseModel):
    question: str

def load_documents():
    docs = []
    for path in DOCS_DIR.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        docs.append({"source": path.name, "text": text})
    return docs

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def build_chunks():
    all_chunks = []
    for doc in load_documents():
        for chunk in chunk_text(doc["text"]):
            all_chunks.append({
                "source": doc["source"],
                "content": chunk
            })
    return all_chunks

def tokenize(text):
    return set(re.findall(r"\b[a-zA-Z0-9_]+\b", text.lower()))

def retrieve(question, top_k=3):
    q_tokens = tokenize(question)
    scored = []
    for chunk in CHUNKS:
        c_tokens = tokenize(chunk["content"])
        score = len(q_tokens.intersection(c_tokens))
        scored.append({
            "score": score,
            "source": chunk["source"],
            "content": chunk["content"]
        })
    scored.sort(key=lambda x: x["score"], reverse=True)
    return [x for x in scored[:top_k] if x["score"] > 0]

def generate_answer(question, retrieved_chunks):
    if not retrieved_chunks:
        return "I could not find relevant context in the loaded documents."
    context_summary = "\n\n".join(
        f"Source: {c['source']}\n{c['content']}" for c in retrieved_chunks
    )
    return (
        "Based on the retrieved documents, here is a grounded response:\n\n"
        f"{context_summary}\n\n"
        f"Question: {question}\n\n"
        "In a full version, this context would be passed to an LLM to produce a concise final answer."
    )

@app.on_event("startup")
def startup_event():
    global CHUNKS
    CHUNKS = build_chunks()

@app.post("/ask")
def ask(req: AskRequest):
    start = time.time()
    retrieved = retrieve(req.question, top_k=3)
    answer = generate_answer(req.question, retrieved)
    latency_ms = round((time.time() - start) * 1000, 2)

    return {
        "question": req.question,
        "answer": answer,
        "sources": list({c["source"] for c in retrieved}),
        "retrieved_chunks": retrieved,
        "latency_ms": latency_ms
    }
