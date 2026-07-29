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
        "user_query": request.user_query,
        "shipment_id": request.shipment_id,
        "shipment_status": "",
        "weather": "",
        "supplier_status": "",
        "warehouse_status": "",
        "risk_level": "",
        "retrieved_documents": [],
        "messages": [],
        "tool_results": [],
        "final_response": "",
    }

    result = app.invoke(
        state,
        config=DEFAULT_SESSION,
    )

    return ChatResponse(
        response=result["final_response"]
    )
