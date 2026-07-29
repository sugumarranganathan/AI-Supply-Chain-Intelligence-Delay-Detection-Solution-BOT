"""
Customer Lookup Tool
"""

import pandas as pd
from langchain_core.tools import tool

df = pd.read_csv("data/customer_data.csv")
df.columns = df.columns.str.strip()


@tool
def find_shipment(customer_input: str) -> str:
    """
    Find Shipment ID using phone, email, order ID or customer name.
    """

    customer_input = customer_input.strip().lower()

    for _, row in df.iterrows():

        if (
            str(row["Phone"]).lower() == customer_input
            or str(row["Email"]).lower() == customer_input
            or str(row["OrderID"]).lower() == customer_input
            or str(row["CustomerName"]).lower() == customer_input
        ):
            return row["ShipmentID"]

    return "NOT_FOUND"
