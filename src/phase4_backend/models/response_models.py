from pydantic import BaseModel

class AskResponse(BaseModel):
    answer: str

class CorrectResponse(BaseModel):
    correction: str
