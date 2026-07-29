"""
Business Logic Nodes for LangGraph
"""

from langchain_core.output_parsers import StrOutputParser

from src.graph.state import SupplyChainState

from src.tools.shipment_tool import (
    get_shipment_details,
    get_shipment_status,
)
from src.tools.customer_lookup_tool import find_shipment
from src.tools.weather_tool import get_weather
from src.tools.supplier_tool import get_supplier_status
from src.tools.risk_tool import calculate_delay_risk

from src.models.llm import LLMFactory
from src.rag.retriever import DocumentRetriever


# ==================================================
# Initialize Components
# ==================================================

llm = LLMFactory.create()

retriever = DocumentRetriever()

parser = StrOutputParser()


# ==================================================
# Input Node
# ==================================================

def input_node(state: SupplyChainState):
    """
    Entry point of the workflow.
    """

    print("=" * 60)
    print("Input Node")
    print("=" * 60)

    return state


# ==================================================
# Customer Lookup Node
# ==================================================

def customer_lookup_node(state: SupplyChainState):
    """
    Find Shipment ID using customer information.
    """

    print("=" * 60)
    print("Customer Lookup Node")
    print("=" * 60)

    customer_input = state.get("customer_input", "").strip()

    # If Shipment ID is already available, skip lookup
    if state.get("shipment_id", "").strip():
        return state

    # If no customer information is provided
    if not customer_input:
        print("No customer information provided.")
        return state

    shipment_id = find_shipment.invoke(
        {
            "customer_input": customer_input
        }
    )

    if shipment_id == "NOT_FOUND":
        print("Customer not found.")

        state["shipment_id"] = ""
        state["final_response"] = (
            "Customer details not found. "
            "Please verify the phone number, email, order ID or customer name."
        )

        return state
    
    else:
        print(f"Shipment Found: {shipment_id}")
        state["shipment_id"] = shipment_id

    return state


# ==================================================
# Retriever Node (RAG)
# ==================================================

def retriever_node(state: SupplyChainState):
    """
    Retrieve relevant documents from the FAISS vector database.
    """

    print("=" * 60)
    print("Retriever Node")
    print("=" * 60)

    query = state.get("user_query", "")

    documents = retriever.retrieve(query)

    state["retrieved_documents"] = [
        doc.page_content
        for doc in documents
    ]

    return state



# ==================================================
# Shipment Node
# ==================================================

def shipment_node(state: SupplyChainState):
    """
    Fetch complete shipment information.
    """

    print("=" * 60)
    print("Shipment Node")
    print("=" * 60)

    shipment_id = state.get("shipment_id", "")

    shipment = get_shipment_details.invoke(
        {
            "shipment_id": shipment_id
        }
    )

    if shipment["status"] == "Shipment Not Found":
        state["final_response"] = (
            f"Shipment '{shipment_id}' was not found."
        )
        return state

    state["shipment_status"] = shipment["status"]
    state["supplier_id"] = shipment["supplier_id"]
    state["warehouse_id"] = shipment["warehouse_id"]
    state["destination_city"] = shipment["destination_city"]

    print(f"Shipment ID      : {shipment_id}")
    print(f"Status           : {shipment['status']}")
    print(f"Supplier ID      : {shipment['supplier_id']}")
    print(f"Warehouse ID     : {shipment['warehouse_id']}")
    print(f"Destination City : {shipment['destination_city']}")

    return state
    


# ==================================================
# Weather Node
# ==================================================

# ==================================================
# Weather Node
# ==================================================

def weather_node(state: SupplyChainState):
    """
    Fetch weather information dynamically.
    """

    print("=" * 60)
    print("Weather Node")
    print("=" * 60)

    city = state.get("destination_city", "")

    weather = get_weather.invoke(
        {
            "city": city
        }
    )

    state["weather"] = weather

    print(f"Destination City : {city}")
    print(f"Weather          : {weather}")

    return state

# ==================================================
# Supplier Node
# ==================================================
# ==================================================
# Supplier Node
# ==================================================

def supplier_node(state: SupplyChainState):
    """
    Fetch supplier status dynamically from Shipment Details.
    """

    print("=" * 60)
    print("Supplier Node")
    print("=" * 60)

    supplier_id = state.get("supplier_id", "")

    supplier = get_supplier_status.invoke(
        {
            "supplier_id": supplier_id
        }
    )

    state["supplier_status"] = supplier

    print(f"Supplier ID     : {supplier_id}")

    if supplier == "Supplier not found.":
        print("Supplier not found.")
    else:
        print(f"Supplier Status : {supplier}")

    return state
# ==================================================
# Risk Node
# ==================================================

def risk_node(state: SupplyChainState):
    """
    Analyze shipment delay risk.
    """

    print("=" * 60)
    print("Risk Node")
    print("=" * 60)

    shipment_status = state.get("shipment_status", "")
    weather = state.get("weather", "")
    supplier_status = state.get("supplier_status", "")

    risk = calculate_delay_risk.invoke(
        {
            "shipment_status": shipment_status,
            "weather": weather,
            "supplier_status": supplier_status,
        }
    )

    state["risk_level"] = risk

    return state


# ==================================================
# LLM Node
# ==================================================

def llm_node(state: SupplyChainState):
    """
    Generate the final AI logistics report using
    RAG + Tool Results.
    """

    print("=" * 60)
    print("LLM Node")
    print("=" * 60)

    context = "\n\n".join(
        state.get("retrieved_documents", [])
    )

    prompt = f"""
You are an expert AI Supply Chain Intelligence Assistant.

Use the retrieved knowledge base and live shipment information
to answer professionally.

==================================================
KNOWLEDGE BASE
==================================================

{context}

==================================================
LIVE SHIPMENT INFORMATION
==================================================

Shipment ID:
{state.get("shipment_id", "Unknown")}

Shipment Status:
{state.get("shipment_status", "Unknown")}

Weather:
{state.get("weather", "Not Available")}

Supplier Status:
{state.get("supplier_status", "Not Available")}

Warehouse Status:
{state.get("warehouse_status", "Not Available")}

Risk Level:
{state.get("risk_level", "Unknown")}

==================================================
USER QUESTION
==================================================

{state.get("user_query", "")}

==================================================
Instructions
==================================================

Answer using the Knowledge Base first.

If the answer is not available in the Knowledge Base,
use the live shipment information.

Generate a professional report with the following sections:

1. Executive Summary

2. Shipment Status

3. Weather Impact

4. Supplier Analysis

5. Risk Assessment

6. Recommended Actions

7. Estimated Business Impact

Keep the report concise and professional.
"""

    response = llm.invoke(prompt)

    final_response = parser.invoke(response)

    state["final_response"] = final_response

    state.setdefault("messages", [])

    state["messages"].append(
        f"User: {state.get('user_query', '')}"
    )

    state["messages"].append(
        f"Assistant: {final_response}"
    )

    return state


# ==================================================
# Output Node
# ==================================================

# ==================================================
# Output Node
# ==================================================

def output_node(state: SupplyChainState):
    """
    Final workflow node.
    """

    print("=" * 60)
    print("Output Node")
    print("=" * 60)

    # Do not print the response here.
    # Just return the final state.

    return state
