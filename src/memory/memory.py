"""
LangGraph Memory Configuration
"""

from langgraph.checkpoint.memory import InMemorySaver


def get_memory():
    """
    Create an in-memory checkpoint for LangGraph.

    Suitable for development and testing.
    """

    return InMemorySaver()
