"""
Conversation Buffer Memory
"""

from langchain.memory import ConversationBufferMemory


def get_buffer_memory():
    """
    Returns a ConversationBufferMemory instance.
    """
    return ConversationBufferMemory(
        return_messages=True
    )
