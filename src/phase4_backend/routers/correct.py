from fastapi import APIRouter, HTTPException
from src.phase4_backend.models.request_models import CorrectRequest
from src.phase4_backend.models.response_models import CorrectResponse
from src.phase4_backend.services.rag_service import retrieve_context
from src.phase4_backend.services.llm_service import correct_exercise
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/correct", response_model=CorrectResponse)
async def correct_exercise_endpoint(request: CorrectRequest):
    try:
        context = retrieve_context(request.exercise_text, request.subject, request.session_id)
        correction = correct_exercise(context, request.exercise_text)
        return CorrectResponse(correction=correction)
    except Exception as e:
        logger.error(f"Error in correct_exercise: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
