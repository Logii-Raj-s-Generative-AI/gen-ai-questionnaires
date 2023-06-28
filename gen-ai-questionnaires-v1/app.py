from fastapi import FastAPI
import logging
from datetime import datetime
import uvicorn


# define logging format
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = FastAPI()


def get_current_timestamp():
    timestamp = datetime.now()
    formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_timestamp

@app.get("/")
async def root():
    return {"message": "gen-ai app is UP!"}

@app.get("/v1")
async def greeting():
    return { "message": "Hello from gen-ai!"}