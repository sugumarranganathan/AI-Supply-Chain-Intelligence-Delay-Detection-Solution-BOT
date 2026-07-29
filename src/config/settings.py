"""
Application Configuration
-------------------------
Loads environment variables and provides
centralized configuration for the project.
"""

import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


class Settings:
    """
    Central configuration class.
    """

    # ==========================
    # API Keys
    # ==========================

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    # ==========================
    # LLM Configuration
    # ==========================

    DEFAULT_MODEL = "llama-3.3-70b-versatile"

    TEMPERATURE = 0.3

    MAX_TOKENS = 1024


settings = Settings()
