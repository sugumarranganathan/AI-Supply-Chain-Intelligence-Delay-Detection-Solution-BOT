"""
AI Supply Chain Intelligence
Delay Detection & Solution BOT

Gradio Application
Part 1
"""

# ==========================================================
# IMPORTS
# ==========================================================

import gradio as gr
from src.graph.workflow import create_workflow
from src.memory.session import DEFAULT_SESSION
from src.validation.validator import validate_input

# ==========================================================
# CREATE WORKFLOW
# ==========================================================

workflow = create_workflow()

# ==========================================================
# THEME
# ==========================================================

theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="green",
    neutral_hue="slate"
)

# ==========================================================
# CSS
# ==========================================================

css = """
.gradio-container{
    max-width:1400px !important;
    margin:auto;
}

h1,h2,h3{
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
}
"""

# ==========================================================
# DUMMY FUNCTION
# (Real LangGraph comes in Part 2)
# ==========================================================
# ==========================================================
# ANALYZE SHIPMENT
# ==========================================================


def analyze(search_method, search_value, question):

    shipment_id = ""
    customer_input = ""

    # ------------------------------------------
    # INPUT VALIDATION
    # ------------------------------------------

    error = validate_input(
        search_method,
        search_value,
        question
    )

    if error:
        return (
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            f"# ❌ Validation Error\n\n{error}"
        )

    # ------------------------------------------
    # Normalize Search Value
    # ------------------------------------------
    
    
    
    elif search_method == "Email":
        search_value = search_value.lower()
    
    elif search_method == "Customer Name":
        search_value = search_value.title()

    # ------------------------------------------
    # Determine Search Type
    # ------------------------------------------
    
    if search_method == "Shipment ID":
        shipment_id = search_value
    else:
        customer_input = search_value
        # ------------------------------------------
        # Initial LangGraph State
        # ------------------------------------------

    state = {

        # User Query
        "user_query": question,

        # Customer Information
        "customer_input": customer_input,
        "customer_name": "",
        "phone": "",
        "email": "",
        "order_id": "",

        # Shipment Information
        "shipment_id": shipment_id,
        "shipment_status": "",
        "supplier_id": "",
        "warehouse_id": "",
        "destination_city": "",

        # External Tool Results
        "weather": "",
        "supplier_status": "",
        "warehouse_status": "",

        # Risk
        "risk_level": "",

        # RAG
        "retrieved_documents": [],

        # Conversation Memory
        "messages": [],

        # Tool Logs
        "tool_results": [],

        # Final Response
        "final_response": ""
    }

    # ------------------------------------------
    # Execute LangGraph
    # ------------------------------------------

    try:

        result = workflow.invoke(
            state,
            config=DEFAULT_SESSION
        )

    except Exception as e:

        return (
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            f"# ❌ Error\n\n{str(e)}"
        )

    # ------------------------------------------
    # Return Results to Gradio
    # ------------------------------------------

    return (

        result.get("shipment_id", ""),

        result.get("shipment_status", ""),

        result.get("supplier_id", ""),

        result.get("warehouse_id", ""),

        result.get("destination_city", ""),

        result.get("weather", ""),

        result.get("risk_level", ""),

        result.get(
            "final_response",
            "No response generated."
        )

    )

# ==========================================================
# UI
# ==========================================================

with gr.Blocks(
    theme=theme,
    css=css,
    title="AI Supply Chain Intelligence"
) as demo:

    gr.Markdown("""
# 🚚 AI Supply Chain Intelligence

## Delay Detection & Solution BOT
""")

    with gr.Row():

        search_method = gr.Dropdown(

            choices=[
                "Shipment ID",
                "Mobile Number",
                "Email",
                "Order ID",
                "Customer Name"
            ],

            value="Shipment ID",

            label="Search Method"

        )

        search_value = gr.Textbox(

            label="Search Value",

            placeholder="Enter Shipment ID / Mobile / Email"

        )

    question = gr.Textbox(

        label="Ask Your Question",

        placeholder="Example: Where is my shipment?",

        lines=3

    )

    analyze_btn = gr.Button(

        "🚀 Analyze Shipment",

        variant="primary"

    )

    gr.Markdown("---")

    gr.Markdown("## 📊 Shipment Dashboard")

    with gr.Row():

        shipment_id = gr.Textbox(
            label="Shipment ID",
            interactive=False
        )

        shipment_status = gr.Textbox(
            label="Shipment Status",
            interactive=False
        )

    with gr.Row():

        supplier = gr.Textbox(
            label="Supplier ID",
            interactive=False
        )

        warehouse = gr.Textbox(
            label="Warehouse",
            interactive=False
        )

    with gr.Row():

        destination = gr.Textbox(
            label="Destination",
            interactive=False
        )

        weather = gr.Textbox(
            label="Weather",
            interactive=False
        )

    risk = gr.Textbox(

        label="Risk Level",

        interactive=False

    )

    gr.Markdown("## 🤖 AI Response")

    ai_report = gr.Markdown()

    analyze_btn.click(

        fn=analyze,

        inputs=[
            search_method,
            search_value,
            question
        ],

        outputs=[
            shipment_id,
            shipment_status,
            supplier,
            warehouse,
            destination,
            weather,
            risk,
            ai_report
        ]

    )

    gr.Markdown("""

---

### Built with LangGraph • LangChain • RAG • Groq

""")

# ==========================================================
# START APPLICATION
# ==========================================================

if __name__ == "__main__":

    demo.launch(share=True)
