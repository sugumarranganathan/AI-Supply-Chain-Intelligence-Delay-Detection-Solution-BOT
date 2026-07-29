"""
Risk Assessment Chain
"""

from langchain_core.output_parsers import StrOutputParser

from src.models.llm import LLMFactory
from src.prompts.base_prompt import create_prompt
from src.prompts.system_prompt import SYSTEM_PROMPT


RISK_PROMPT = """
Analyse the shipment status below.

Status:
{status}

Provide:

- Risk Level
- Reason
- Suggested Action
"""


def create_risk_chain():

    llm = LLMFactory.create()

    prompt = create_prompt(
        SYSTEM_PROMPT,
        RISK_PROMPT
    )

    parser = StrOutputParser()

    return prompt | llm | parser
