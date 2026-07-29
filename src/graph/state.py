"""
Application State for LangGraph
"""

from typing import List, TypedDict


class SupplyChainState(TypedDict):
    """
    Shared application state passed between LangGraph nodes.
    """

    # ==========================================================
    # User Input
    # ==========================================================

    user_query: str

    # ==========================================================
    # Shipment Information
    # ==========================================================

    shipment_id: str
    shipment_status: str

    # ==========================================================
    # External Tool Results
    # ==========================================================

    weather: str
    supplier_status: str
    warehouse_status: str

    # ==========================================================
    # Risk Analysis
    # ==========================================================

    risk_level: str

    # ==========================================================
    # RAG Context
    # ==========================================================

    retrieved_documents: List[str]

    # ==========================================================
    # Conversation Memory
    # ==========================================================

    messages: List[str]

    # ==========================================================
    # Tool Execution Log (Optional)
    # ==========================================================

    tool_results: List[str]

    # ==========================================================
    # Final AI Response
    # ==========================================================

    final_response: str