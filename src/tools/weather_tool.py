"""
Weather Tool
"""

from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """
    Returns weather information.
    """

    weather = {
        "Chennai": "Sunny, 34°C",
        "Mumbai": "Heavy Rain, 29°C",
        "Delhi": "Cloudy, 31°C",
    }

    return weather.get(city, "Weather data unavailable.")
