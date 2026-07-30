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

        print("Do you know your Shipment ID?")
        print("1. Yes")
        print("2. No")

        choice = input("Choose (1/2) or 'exit': ").strip()

        if choice.lower() == "exit":
            print("\nThank you for using AI Supply Chain Intelligence.")
            break

        shipment_id = ""
        customer_input = ""

        if choice == "1":

            shipment_id = input("Enter Shipment ID: ").strip()

            if shipment_id.lower() == "exit":
                print("\nThank you for using AI Supply Chain Intelligence.")
                break

        elif choice == "2":

            print("\nSearch using one of the following:")
            print("• Mobile Number")
            print("• Email")
            print("• Order ID")
            print("• Customer Name")

            customer_input = input("Enter value: ").strip()

            if customer_input.lower() == "exit":
                print("\nThank you for using AI Supply Chain Intelligence.")
                break

        else:
            print("\nInvalid choice. Please select 1 or 2.\n")
            continue

        user_query = input("\nAsk your question: ").strip()

        # --------------------------------------------------
        # Initial State
        # --------------------------------------------------

        state = {

            # ==================================================
            # User Input
            # ==================================================

            "user_query": user_query,

            # ==================================================
            # Customer Information
            # ==================================================

            "customer_input": customer_input,
            "customer_name": "",
            "phone": "",
            "email": "",
            "order_id": "",

            # ==================================================
            # Shipment Information
            # ==================================================

            "shipment_id": shipment_id,
            "shipment_status": "",
            "supplier_id": "",
            "warehouse_id": "",
            "destination_city": "",

            # ==================================================
            # External Tool Results
            # ==================================================

            "weather": "",
            "supplier_status": "",
            "warehouse_status": "",

            # ==================================================
            # Risk Analysis
            # ==================================================

            "risk_level": "",

            # ==================================================
            # RAG Context
            # ==================================================

            "retrieved_documents": [],

            # ==================================================
            # Conversation Memory
            # ==================================================

            "messages": [],

            # ==================================================
            # Tool Execution Log
            # ==================================================

            "tool_results": [],

            # ==================================================
            # Final Response
            # ==================================================

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
