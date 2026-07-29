"""
Supplier Tool
"""

from langchain_core.tools import tool


@tool
def get_supplier_status(supplier_name: str) -> str:
    """
    Returns supplier status.
    """

    suppliers = {
        "ABC Logistics": "Active",
        "XYZ Transport": "Delayed Deliveries",
        "Global Freight": "Operational",
    }

    return suppliers.get(
        supplier_name,
        "Supplier not found."
    )
