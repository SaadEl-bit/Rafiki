import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.phase4_backend.routers import ask, correct

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Rafiki AI Tutor API")

allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ask.router, prefix="/api", tags=["Ask"])
app.include_router(correct.router, prefix="/api", tags=["Correct"])

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Rafiki Backend is running"}
