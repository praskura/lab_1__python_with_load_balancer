import os
import asyncpg
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
    conn = await asyncpg.connect(dsn=settings.database_dsn)

    result = [dict(v) for v in await conn.fetch('SELECT * FROM wild_animals')]

    await conn.close()

    return {"data": result}
