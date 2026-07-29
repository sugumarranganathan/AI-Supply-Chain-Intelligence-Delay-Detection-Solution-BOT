"""
API Request / Response Models
"""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Request model for AI chatbot.
    """

    shipment_id: str = Field(
        default="",
        description="Shipment ID (optional)"
    )

    customer_input: str = Field(
        default="",
        description="Phone, Email, Order ID or Customer Name (optional)"
    )

    user_query: str = Field(
        ...,
        description="User question"
    )


class ChatResponse(BaseModel):
    """
    AI chatbot response.
    """

    shipment_id: str

    response: str
