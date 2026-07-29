"""
Pydantic Output Parser
"""

from langchain_core.output_parsers import PydanticOutputParser

from src.parsers.models import ShipmentAnalysis


def get_pydantic_parser():
    """
    Returns a Pydantic parser.
    """
    return PydanticOutputParser(
        pydantic_object=ShipmentAnalysis
    )
