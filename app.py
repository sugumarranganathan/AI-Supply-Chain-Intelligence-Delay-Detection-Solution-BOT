"""
AI Supply Chain Intelligence
Delay Detection & Solution BOT

Main Application Entry Point
"""

from src.graph.workflow import create_workflow
from src.memory.session import DEFAULT_SESSION


def main():
    """
    Main application entry point.
    """

    print("=" * 60)
    print("AI Supply Chain Intelligence")
    print("Delay Detection & Solution BOT")
    print("=" * 60)

    # --------------------------------------------------
    # Create LangGraph Workflow
    # --------------------------------------------------

    app = create_workflow()

    print("Workflow initialized successfully.\n")

    while True:

        print("-" * 60)

        shipment_id = input("Enter Shipment ID (or 'exit'): ").strip()

        if shipment_id.lower() == "exit":
            print("\nThank you for using AI Supply Chain Intelligence.")
            break

        user_query = input("Ask your question: ").strip()

        # --------------------------------------------------
        # Initial State
        # --------------------------------------------------

        state = {
            "user_query": user_query,
            "shipment_id": shipment_id,
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

        # --------------------------------------------------
        # Execute Workflow
        # --------------------------------------------------

        result = app.invoke(
            state,
            config=DEFAULT_SESSION,
        )

        print("\n" + "=" * 60)
        print("AI RESPONSE")
        print("=" * 60)
        print(result["final_response"])
        print("=" * 60 + "\n")


if __name__ == "__main__":
    main()