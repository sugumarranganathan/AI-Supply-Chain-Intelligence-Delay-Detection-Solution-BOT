"""
Supply Chain Workflow
"""

from langgraph.graph import StateGraph, END

from src.graph.state import SupplyChainState

from src.memory.memory import get_memory

from src.graph.nodes import (
    input_node,
    retriever_node,
    shipment_node,
    weather_node,
    supplier_node,
    risk_node,
    llm_node,
    output_node,
    route_after_shipment,
)


def create_workflow():
    """
    Build and compile the Supply Chain LangGraph workflow.
    """

    # ==========================================================
    # Create Workflow
    # ==========================================================

    workflow = StateGraph(SupplyChainState)

    # ==========================================================
    # Register Nodes
    # ==========================================================

    workflow.add_node("input", input_node)
    workflow.add_node("retriever", retriever_node)
    workflow.add_node("shipment", shipment_node)
    workflow.add_node("weather", weather_node)
    workflow.add_node("supplier", supplier_node)
    workflow.add_node("risk", risk_node)
    workflow.add_node("llm", llm_node)
    workflow.add_node("output", output_node)

    # ==========================================================
    # Entry Point
    # ==========================================================

    workflow.set_entry_point("input")

    # ==========================================================
    # Workflow
    # ==========================================================

    # Input → Retriever
    workflow.add_edge("input", "retriever")

    # Retriever → Shipment
    workflow.add_edge("retriever", "shipment")

    # Shipment → Weather / Supplier / Risk
    workflow.add_conditional_edges(
        "shipment",
        route_after_shipment,
        {
            "weather": "weather",
            "supplier": "supplier",
            "risk": "risk",
        },
    )

    # ==========================================================
    # Parallel Branches
    # ==========================================================

    workflow.add_edge("weather", "risk")
    workflow.add_edge("supplier", "risk")

    # ==========================================================
    # Final Flow
    # ==========================================================

    workflow.add_edge("risk", "llm")
    workflow.add_edge("llm", "output")
    workflow.add_edge("output", END)

    # ==========================================================
    # Compile Workflow
    # ==========================================================

    memory = get_memory()

    app = workflow.compile(
    checkpointer=memory
    )
    return app