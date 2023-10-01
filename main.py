import os
from fastapi import FastAPI
from pydantic_settings import BaseSettings
from settings import Settings

app = FastAPI()


@app.get("/health_check")
async def health_check():
    settings = Settings()

    return {"state": "OK", "replica": settings.replica}
