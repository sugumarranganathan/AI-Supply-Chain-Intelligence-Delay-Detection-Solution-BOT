"""
Warehouse Tool
"""

from langchain_core.tools import tool


@tool
def get_warehouse_capacity(location: str) -> str:
    """
    Returns warehouse capacity.
    """

    capacity = {
        "Chennai": "82% Full",
        "Bangalore": "67% Full",
        "Hyderabad": "91% Full",
    }

    return capacity.get(
        location,
        "Warehouse not found."
    )
