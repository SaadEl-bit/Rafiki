from pydantic import BaseModel
from typing import Optional

class AskRequest(BaseModel):
    question: str
    subject: str
    session_id: Optional[str] = None

class CorrectRequest(BaseModel):
    exercise_text: str
    subject: str
    session_id: str  # Required: user must upload a document first
