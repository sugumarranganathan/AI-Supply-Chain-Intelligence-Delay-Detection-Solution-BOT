"""
Conversation Summary Memory
"""

from langchain.memory import ConversationSummaryMemory

from src.models.llm import LLMFactory


def get_summary_memory():
    """
    Returns a ConversationSummaryMemory instance.
    """
    return ConversationSummaryMemory(
        llm=LLMFactory.create(),
        return_messages=True
    )
