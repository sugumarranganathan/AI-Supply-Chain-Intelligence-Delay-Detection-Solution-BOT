"""
Groq Language Model
"""

from langchain_groq import ChatGroq

from src.config.settings import settings


class LLMFactory:
    """
    Factory class for creating LLM instances.
    """

    @staticmethod
    def create():

        return ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model=settings.DEFAULT_MODEL,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
        )
