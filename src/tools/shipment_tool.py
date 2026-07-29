import pandas as pd
from langchain_core.tools import tool

df = pd.read_csv("data/shipment_data.csv")


@tool
def get_shipment_status(shipment_id: str) -> str:
    """
    Return shipment status for a shipment ID.
    """

    shipment = df[df["ShipmentID"] == shipment_id]

    if shipment.empty:
        return "Not Found"

    return shipment.iloc[0]["Status"]
