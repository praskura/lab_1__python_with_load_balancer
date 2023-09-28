import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check")
async def health_check():
    replica = os.getenv("REPLICA")

    return {"state": "OK", "replica": replica}
