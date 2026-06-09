from pydantic import BaseModel
from typing import Optional

class AskResponse(BaseModel):
    answer: str
    session_id: Optional[str] = None

class CorrectResponse(BaseModel):
    correction: str
