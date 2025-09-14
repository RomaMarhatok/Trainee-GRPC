import uvicorn

from fastapi import FastAPI
from .routes import note_router

fast_app = FastAPI()
fast_app.include_router(note_router)


async def start_fastapi_server():
    config = uvicorn.Config(
        "api.main:fast_app", host="0.0.0.0", port=8888, log_level="info"
    )
    server = uvicorn.Server(config)
    await server.serve()
