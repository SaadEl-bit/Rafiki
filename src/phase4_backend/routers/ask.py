from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from src.phase4_backend.models.request_models import AskRequest
from src.phase4_backend.models.response_models import AskResponse
from src.phase4_backend.services.rag_service import retrieve_context, add_to_session_rag
from src.phase4_backend.services.extraction_service import file_to_base64_images, extract_text_via_vl
from src.phase4_backend.services.llm_service import generate_answer
import logging
import uuid

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...), subject: str = Form(...)):
    try:
        file_bytes = await file.read()
        filename = file.filename
        
        # 1. Convert to base64 images
        base64_images = file_to_base64_images(file_bytes, filename)
        
        # 2. Extract text using Vision API
        extracted_text = extract_text_via_vl(base64_images)
        
        # 3. Add to Temporary RAG
        session_id = str(uuid.uuid4())
        add_to_session_rag(session_id, extracted_text, subject)
        
        return {
            "session_id": session_id,
            "extracted_text": extracted_text
        }
    except Exception as e:
        logger.error(f"Error in upload_document: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ask", response_model=AskResponse)
async def ask_question(request: AskRequest):
    try:
        context = retrieve_context(request.question, request.subject, request.session_id)
        answer = generate_answer(context, request.question)
        return AskResponse(answer=answer)
    except Exception as e:
        logger.error(f"Error in ask_question: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
