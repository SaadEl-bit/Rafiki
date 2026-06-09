from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from src.phase4_backend.services.exercise_service import generate_exercise, get_topics
from src.phase4_backend.services.exam_service import generate_exam
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

class ExerciseRequest(BaseModel):
    subject: str
    topic: str

    @field_validator("subject")
    @classmethod
    def validate_subject(cls, v):
        allowed = {"maths", "physics", "english"}
        if v not in allowed:
            raise ValueError(f"Subject must be one of: {', '.join(allowed)}")
        return v

class ExamRequest(BaseModel):
    subject: str
    topic: Optional[str] = ""

    @field_validator("subject")
    @classmethod
    def validate_subject(cls, v):
        allowed = {"maths", "physics", "english"}
        if v not in allowed:
            raise ValueError(f"Subject must be one of: {', '.join(allowed)}")
        return v

@router.get("/generate/topics")
async def get_available_topics():
    try:
        return get_topics()
    except Exception as e:
        logger.error(f"Error fetching topics: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/exercise")
async def create_exercise(req: ExerciseRequest):
    try:
        result = generate_exercise(req.subject, req.topic)
        return result
    except Exception as e:
        logger.error(f"Error generating exercise: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate/exam")
async def create_exam(req: ExamRequest):
    try:
        result = generate_exam(req.subject, req.topic)
        return result
    except Exception as e:
        logger.error(f"Error generating exam: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
