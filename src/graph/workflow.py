"""
Supply Chain Workflow
"""

from langgraph.graph import StateGraph, END

from src.graph.state import SupplyChainState
from src.memory.memory import get_memory

from src.graph.nodes import (
    input_node,
    customer_lookup_node,
    retriever_node,
    shipment_node,
    weather_node,
    supplier_node,
    risk_node,
    llm_node,
    output_node,
)


def create_workflow():
    """
    Build and compile the Supply Chain LangGraph workflow.
    """

    workflow = StateGraph(SupplyChainState)

    # ==========================================================
    # Register Nodes
    # ==========================================================

    workflow.add_node("input", input_node)
    workflow.add_node("customer_lookup", customer_lookup_node)
    workflow.add_node("retriever", retriever_node)
    workflow.add_node("shipment", shipment_node)
    workflow.add_node("supplier", supplier_node)
    workflow.add_node("weather", weather_node)
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

    workflow.add_edge("input", "customer_lookup")
    workflow.add_edge("customer_lookup", "retriever")
    workflow.add_edge("retriever", "shipment")

    # Always check supplier
    workflow.add_edge("shipment", "supplier")

    # Then weather
    workflow.add_edge("supplier", "weather")

    # Then risk analysis
    workflow.add_edge("weather", "risk")

    # AI Response
    workflow.add_edge("risk", "llm")
    workflow.add_edge("llm", "output")
    workflow.add_edge("output", END)

    # ==========================================================
    # Compile
    # ==========================================================

    memory = get_memory()

    app = workflow.compile(
        checkpointer=memory
    )

    return app
