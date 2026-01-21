from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SnippetCreate(BaseModel):
    title: str
    content: str
    language: str
    tags: Optional[str] = None

class SnippetUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    language: Optional[str] = None
    tags: Optional[str] = None

class SnippetResponse(BaseModel):
    id: str
    title: str
    content: str
    language: str
    tags: Optional[str] = None
    created_at: datetime

    model_config = {
        "from_attributes": True
    }