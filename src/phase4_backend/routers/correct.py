import re
from fastapi import APIRouter, HTTPException
from src.phase4_backend.models.request_models import CorrectRequest
from src.phase4_backend.models.response_models import CorrectResponse
from src.phase4_backend.services.rag_service import retrieve_context, session_exists
from src.phase4_backend.services.llm_service import correct_exercise
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

def sanitize_exercise_text(text: str) -> str:
    text = re.sub(r'\[Image\s*\d+\]', '', text)
    text = re.sub(r'\[image\s*\d+\]', '', text)
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\\documentclass\{.*?\}', '', text)
    text = re.sub(r'\\usepackage\[.*?\]\{.*?\}', '', text)
    text = re.sub(r'\\usepackage\{.*?\}', '', text)
    text = re.sub(r'---\s*Page\s*\d+\s*---', '', text)
    text = re.sub(r'(?i)^Le document contient\s*.*?\.', '', text)
    text = re.sub(r'(?i)^Ce document\s*.*?\.', '', text)
    text = re.sub(r'(?i)^L\'image\s*.*?\.', '', text)
    text = re.sub(r'(?i)^Cette image\s*.*?\.', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

@router.post("/correct", response_model=CorrectResponse)
async def correct_exercise_endpoint(request: CorrectRequest):
    try:
        if not request.session_id or not session_exists(request.session_id):
            raise HTTPException(
                status_code=400,
                detail="Vous devez d'abord importer un document (PDF ou image) contenant l'exercice à corriger."
            )

        clean_text = sanitize_exercise_text(request.exercise_text)
        context = retrieve_context(clean_text, request.subject, request.session_id)
        correction = correct_exercise(context, clean_text)
        correction = re.sub(r'(?i)ERROR:\s*Cannot read.*?user\.', '', correction)
        # Silent cleanup for any clipboard/image-related errors
        correction = re.sub(r'(?i)(cannot read.*?clipboard|this model does not support image input).*?(\n|$)', '', correction)
        correction = correction.strip()
        return CorrectResponse(correction=correction)
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error in correct_exercise: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
