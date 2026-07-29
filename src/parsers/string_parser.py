"""
String Output Parser
"""

from langchain_core.output_parsers import StrOutputParser


def get_string_parser():
    """
    Returns a string parser.
    """
    return StrOutputParser()
