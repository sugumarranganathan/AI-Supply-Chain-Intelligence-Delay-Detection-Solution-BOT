"""
Conversation Summary Buffer Memory
"""

from langchain.memory import ConversationSummaryBufferMemory

from src.models.llm import LLMFactory


def get_summary_buffer_memory():
    """
    Returns a ConversationSummaryBufferMemory instance.
    """
    return ConversationSummaryBufferMemory(
        llm=LLMFactory.create(),
        max_token_limit=1000,
        return_messages=True
    )
