from fastapi import APIRouter, HTTPException
from src.phase4_backend.services.course_service import get_course, list_courses
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/courses")
async def get_courses_list():
    try:
        return list_courses()
    except Exception as e:
        logger.error(f"Error listing courses: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/course/{subject}")
async def get_course_content(subject: str):
    try:
        data = get_course(subject)
        if "error" in data:
            raise HTTPException(status_code=404, detail=data["error"])
        return data
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching course for {subject}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
