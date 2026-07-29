"""
Shipment Tool
"""

from langchain_core.tools import tool


@tool
def get_shipment_status(shipment_id: str) -> str:
    """
    Returns shipment status.
    """

    shipment_data = {
        "SHIP001": "In Transit",
        "SHIP002": "Delayed",
        "SHIP003": "Delivered",
    }

    return shipment_data.get(
        shipment_id.upper(),
        "Shipment not found."
    )
