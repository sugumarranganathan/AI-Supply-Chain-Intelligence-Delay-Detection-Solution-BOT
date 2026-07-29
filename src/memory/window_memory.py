"""
Conversation Buffer Window Memory
"""

from langchain.memory import ConversationBufferWindowMemory


def get_window_memory():
    """
    Returns a ConversationBufferWindowMemory instance.
    """
    return ConversationBufferWindowMemory(
        k=5,
        return_messages=True
    )
