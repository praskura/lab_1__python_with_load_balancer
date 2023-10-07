import os
from fastapi import FastAPI
from pydantic_settings import BaseSettings
from settings import Settings

app = FastAPI()
settings = Settings()

@app.get("/health_check")
async def health_check():
    return {"state": "OK", "replica": settings.replica}

@app.get("/get_entities")
async def get_entities():
    return {"data": null}
