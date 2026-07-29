"""
Shipment Analysis Chain
"""

from langchain_core.output_parsers import StrOutputParser

from src.models.llm import LLMFactory
from src.prompts.base_prompt import create_prompt
from src.prompts.system_prompt import SYSTEM_PROMPT
from src.prompts.shipment_prompt import SHIPMENT_PROMPT


def create_shipment_chain():
    """
    Create a shipment analysis chain.
    """

    llm = LLMFactory.create()

    prompt = create_prompt(
        SYSTEM_PROMPT,
        SHIPMENT_PROMPT
    )

    parser = StrOutputParser()

    return prompt | llm | parser
