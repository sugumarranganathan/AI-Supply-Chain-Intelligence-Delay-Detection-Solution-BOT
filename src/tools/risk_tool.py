"""
Risk Assessment Tool
"""

from langchain_core.tools import tool


@tool
def calculate_delay_risk(
    shipment_status: str,
    weather: str,
    supplier_status: str,
) -> str:
    """
    Calculate shipment delay risk based on shipment status,
    weather conditions, and supplier status.
    """

    shipment_status = shipment_status.lower()
    weather = weather.lower()
    supplier_status = supplier_status.lower()

    # High Risk
    if (
        shipment_status == "delayed"
        or "storm" in weather
        or "rain" in weather
        or "flood" in weather
        or "delay" in supplier_status
        or "unavailable" in supplier_status
    ):
        return "High Risk"

    # Medium Risk
    if shipment_status == "in transit":
        return "Medium Risk"

    # No Risk
    if shipment_status == "delivered":
        return "No Risk"

    return "Unknown Risk"
