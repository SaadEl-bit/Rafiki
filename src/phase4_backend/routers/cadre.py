from fastapi import APIRouter, HTTPException
from src.phase4_backend.services.cadre_service import get_cadre
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/cadre")
async def list_cadre():
    try:
        return get_cadre()
    except Exception as e:
        logger.error(f"Error fetching cadre: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/cadre/{subject}")
async def get_cadre_subject(subject: str):
    try:
        data = get_cadre(subject)
        if not data or "error" in data[0]:
            raise HTTPException(status_code=404, detail="Subject not found")
        return data[0]
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching cadre for {subject}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
