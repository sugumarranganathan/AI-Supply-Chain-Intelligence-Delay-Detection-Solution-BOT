"""
Input Validation Module

Validates user input before executing the LangGraph workflow.
"""

import re


def validate_input(search_method, search_value, question):
    """
    Validate user input.

    Parameters
    ----------
    search_method : str
        Search type selected by the user.

    search_value : str
        Value entered by the user.

    question : str
        User's question.

    Returns
    -------
    None
        Validation successful.

    str
        Validation error message.
    """

    # ==========================================================
    # Remove Leading / Trailing Spaces
    # ==========================================================

    search_value = search_value.strip()
    question = question.strip()

    # ==========================================================
    # Search Value
    # ==========================================================

    if not search_value:
        return "Please enter a search value."

    # ==========================================================
    # User Question
    # ==========================================================

    if not question:
        return "Please enter your question."

    # ==========================================================
    # Shipment ID Validation
    # Example: SHP1001
    # ==========================================================

    if search_method == "Shipment ID":

        pattern = r"^SHP\d{4}$"

        if not re.fullmatch(pattern, search_value):
            return (
                "Invalid Shipment ID.\n\n"
                "Example: SHP1001"
            )

    # ==========================================================
    # Mobile Number Validation
    # Exactly 10 digits
    # ==========================================================

    elif search_method == "Mobile Number":

        if not search_value.isdigit():
            return "Mobile number must contain only digits."

        if len(search_value) != 10:
            return "Mobile number must contain exactly 10 digits."

    # ==========================================================
    # Email Validation
    # ==========================================================

    elif search_method == "Email":

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(pattern, search_value):
            return (
                "Invalid email address.\n\n"
                "Example: user@gmail.com"
            )

    # ==========================================================
    # Order ID Validation
    # Example: ORD1001
    # ==========================================================

    elif search_method == "Order ID":

        pattern = r"^ORD\d{4}$"

        if not re.fullmatch(pattern, search_value):
            return (
                "Invalid Order ID.\n\n"
                "Example: ORD1001"
            )

    # ==========================================================
    # Customer Name Validation
    # ==========================================================

    elif search_method == "Customer Name":

        if len(search_value) < 3:
            return "Customer name must contain at least 3 characters."

        if not re.fullmatch(r"[A-Za-z ]+", search_value):
            return (
                "Customer name should contain only "
                "alphabetic characters and spaces."
            )

    # ==========================================================
    # Validation Successful
    # ==========================================================

    return None
