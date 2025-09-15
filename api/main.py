from fastapi import FastAPI
from api.routes import note_router

fast_app = FastAPI()
fast_app.include_router(note_router)
