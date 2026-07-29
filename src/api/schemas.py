"""
API Request / Response Models
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    shipment_id: str
    user_query: str


class ChatResponse(BaseModel):
    response: str
