# from fastapi import FastAPI

# # app = FastAPI()
# app = FastAPI(title="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")


# @app.get("/")
# # async def root():
# #     return {"message": "Hello World"}
# def read_root():
#     return {"message": "Welocome to FastAPI!"}

from fastapi import FastAPI
from asyncio import sleep
from datetime import datetime

app = FastAPI()

@app.get("/")
async def async_root():
    await sleep(1)  # Simulate a delay
    return {f"message": f"This message was handled asynchronously at {datetime.now()}!"}
