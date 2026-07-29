"""
Shipment Tool
"""

import pandas as pd
from langchain_core.tools import tool

# Load CSV
df = pd.read_csv("data/shipment_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Clean ShipmentID values
df["ShipmentID"] = df["ShipmentID"].astype(str).str.strip().str.upper()


@tool
def get_shipment_status(shipment_id: str) -> str:
    """
    Return shipment status for a shipment ID.
    """

    shipment_id = shipment_id.strip().upper()

    shipment = df[df["ShipmentID"] == shipment_id]

    if shipment.empty:
        return "Shipment Not Found"

    return shipment.iloc[0]["Status"]
