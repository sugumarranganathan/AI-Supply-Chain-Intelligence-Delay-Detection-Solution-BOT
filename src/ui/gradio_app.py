"""
Gradio Frontend
"""

import requests
import gradio as gr

API_URL = "http://127.0.0.1:8000/chat"


def chat(shipment_id, question):

    payload = {
        "shipment_id": shipment_id,
        "user_query": question,
    }

    try:

        response = requests.post(
            API_URL,
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        return response.json()["response"]

    except Exception as e:

        return f"Error: {e}"


with gr.Blocks(
    title="AI Supply Chain Intelligence"
) as demo:

    gr.Markdown(
        """
# 🚚 AI Supply Chain Intelligence

### Delay Detection & Solution BOT
"""
    )

    shipment = gr.Textbox(
        label="Shipment ID",
        placeholder="SHP1001",
    )

    question = gr.Textbox(
        label="Question",
        lines=4,
        placeholder="Why is my shipment delayed?",
    )

    answer = gr.Textbox(
        label="AI Response",
        lines=14,
    )

    ask = gr.Button("Ask AI")

    ask.click(
        fn=chat,
        inputs=[
            shipment,
            question,
        ],
        outputs=answer,
    )

demo.launch()
