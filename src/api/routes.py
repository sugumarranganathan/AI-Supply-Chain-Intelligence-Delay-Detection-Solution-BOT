"""
API Routes
"""

from fastapi import APIRouter

from src.api.schemas import (
    ChatRequest,
    ChatResponse,
)

from src.graph.workflow import create_workflow
from src.memory.session import DEFAULT_SESSION

router = APIRouter()

app = create_workflow()


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    state = {
        # User Input
        "user_query": request.user_query,
        "shipment_id": request.shipment_id,
        "customer_input": request.customer_input,

        # Shipment Details
        "shipment_status": "",
        "supplier_id": "",
        "warehouse_id": "",
        "destination_city": "",

        # Tool Results
        "weather": "",
        "supplier_status": "",
        "warehouse_status": "",
        "risk_level": "",

        # RAG
        "retrieved_documents": [],

        # Conversation
        "messages": [],
        "tool_results": [],

        # Final Response
        "final_response": "",
    }

    result = app.invoke(
        state,
        config=DEFAULT_SESSION,
    )

    return ChatResponse(
        shipment_id=result.get("shipment_id", ""),
        response=result.get("final_response", ""),
    )
