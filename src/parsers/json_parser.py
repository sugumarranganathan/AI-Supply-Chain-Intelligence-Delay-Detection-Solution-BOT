"""
JSON Output Parser
"""

from langchain_core.output_parsers import JsonOutputParser


def get_json_parser():
    """
    Returns a JSON parser.
    """
    return JsonOutputParser()
