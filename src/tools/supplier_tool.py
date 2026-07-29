"""
Supplier Tool
"""

import pandas as pd
from langchain_core.tools import tool

# Load supplier data
df = pd.read_csv("data/supplier_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Clean values
df["SupplierID"] = df["SupplierID"].astype(str).str.strip().str.upper()


@tool
def get_supplier_status(supplier_id: str) -> str:
    """
    Returns supplier status using Supplier ID.
    """

    supplier_id = supplier_id.strip().upper()

    supplier = df[df["SupplierID"] == supplier_id]

    if supplier.empty:
        return "Supplier not found."

    return supplier.iloc[0]["Status"]
