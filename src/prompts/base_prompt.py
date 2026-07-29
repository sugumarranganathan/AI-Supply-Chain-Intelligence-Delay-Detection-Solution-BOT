"""
Base Prompt Templates
"""

from langchain_core.prompts import ChatPromptTemplate


def create_prompt(system_prompt: str, human_prompt: str):
    """
    Create a reusable chat prompt.
    """

    return ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", human_prompt),
        ]
    )
