"""
Pydantic Models for Output Parsing
"""

from pydantic import BaseModel, Field


class ShipmentAnalysis(BaseModel):
    """
    Structured shipment analysis output.
    """

    shipment_id: str = Field(description="Shipment ID")

    risk_level: str = Field(description="Risk Level")

    delay_days: int = Field(description="Estimated Delay")

    reason: str = Field(description="Reason for delay")

    recommendation: str = Field(description="Suggested action")
