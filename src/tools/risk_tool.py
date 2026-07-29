"""
Risk Assessment Tool
"""

from langchain_core.tools import tool


@tool
def calculate_delay_risk(status: str) -> str:
    """
    Calculates delay risk based on shipment status.
    """

    status = status.lower()

    if status == "delayed":
        return "High Risk"

    if status == "in transit":
        return "Medium Risk"

    if status == "delivered":
        return "No Risk"

    return "Unknown Risk"
