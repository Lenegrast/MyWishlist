from fastapi import FastAPI
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
@app.get("/")
async def root():
    logger.info("Handling request to root endpoint")
    return {"message" : "Hello world"}