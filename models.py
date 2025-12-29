# models.py

from typing import List, Optional
from pydantic import BaseModel
from config import DEFAULT_CODING_MODEL

class Message(BaseModel):
    role: str
    content: str
    image_url: Optional[str] = None

class ChatRequest(BaseModel):
    messages: List[Message]
    web_search: bool = False
    model: str = "auto"
    coding_mode: bool = False
    coding_model: str = DEFAULT_CODING_MODEL
    reasoning_mode: bool = False
