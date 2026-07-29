"""
Summary Chain
"""

from langchain_core.output_parsers import StrOutputParser

from src.models.llm import LLMFactory
from src.prompts.base_prompt import create_prompt
from src.prompts.system_prompt import SYSTEM_PROMPT


SUMMARY_PROMPT = """
Summarise the following logistics report.

{text}
"""


def create_summary_chain():

    llm = LLMFactory.create()

    prompt = create_prompt(
        SYSTEM_PROMPT,
        SUMMARY_PROMPT
    )

    parser = StrOutputParser()

    return prompt | llm | parser
