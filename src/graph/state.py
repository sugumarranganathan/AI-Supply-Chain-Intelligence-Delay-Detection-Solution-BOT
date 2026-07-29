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
    # Customer Information
    # ==========================================================

    customer_input: str
    customer_name: str
    phone: str
    email: str
    order_id: str

    # ==========================================================
    # Shipment Information
    # ==========================================================

    shipment_id: str
    shipment_status: str
    supplier_id: str
    warehouse_id: str
    destination_city: str

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
    # Tool Execution Log
    # ==========================================================

    tool_results: List[str]

    # ==========================================================
    # Final AI Response
    # ==========================================================

    final_response: str
