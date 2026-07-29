"""
Shipment Tool
"""

import pandas as pd
from langchain_core.tools import tool

# ==========================================================
# Load Shipment Data
# ==========================================================

df = pd.read_csv("data/shipment_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Clean Shipment IDs
df["ShipmentID"] = df["ShipmentID"].astype(str).str.strip().str.upper()


# ==========================================================
# Shipment Tool
# ==========================================================

@tool
def get_shipment_details(shipment_id: str) -> dict:
    """
    Return complete shipment details for a Shipment ID.
    """

    shipment_id = shipment_id.strip().upper()

    shipment = df[df["ShipmentID"] == shipment_id]

    if shipment.empty:
        return {
            "shipment_id": shipment_id,
            "status": "Shipment Not Found",
            "supplier_id": "",
            "warehouse_id": "",
            "destination_city": "",
        }

    row = shipment.iloc[0]

    return {
        "shipment_id": row["ShipmentID"],
        "status": row["Status"],
        "supplier_id": row["SupplierID"],
        "warehouse_id": row["WarehouseID"],
        "destination_city": row["DestinationCity"],
    }


# ==========================================================
# Backward Compatibility
# ==========================================================

@tool
def get_shipment_status(shipment_id: str) -> str:
    """
    Return shipment status only.
    """

    details = get_shipment_details.invoke(
        {
            "shipment_id": shipment_id
        }
    )

    return details["status"]
