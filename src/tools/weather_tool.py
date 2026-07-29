"""
Weather Tool
Reads weather information from CSV.
"""

import pandas as pd
from langchain_core.tools import tool


@tool
def get_weather(city: str) -> str:
    """
    Returns weather information for a destination city.
    """

    try:
        # Read CSV
        df = pd.read_csv("data/weather_data.csv")

        # Clean input
        city = city.strip().lower()

        # Find matching city
        result = df[df["City"].str.strip().str.lower() == city]

        if result.empty:
            return "Weather data unavailable."

        return result.iloc[0]["Weather"]

    except Exception as e:
        return f"Weather lookup failed: {str(e)}"
