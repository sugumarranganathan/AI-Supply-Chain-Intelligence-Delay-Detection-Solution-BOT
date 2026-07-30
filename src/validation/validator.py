"""
Input Validation Module
"""

import re


def validate_input(search_method, search_value, question):
    """
    Validate user input before executing LangGraph.

    Returns
    -------
    None
        If validation succeeds.

    str
        Error message if validation fails.
    """

    # -------------------------------------------------
    # Search Value
    # -------------------------------------------------

    if not search_value.strip():
        return "Please enter a search value."

    # -------------------------------------------------
    # Question
    # -------------------------------------------------

    if not question.strip():
        return "Please enter your question."

    # -------------------------------------------------
    # Shipment ID
    # -------------------------------------------------

    if search_method == "Shipment ID":

        pattern = r"^SHP\d{4}$"

        if not re.fullmatch(pattern, search_value):

            return (
                "Invalid Shipment ID.\n\n"
                "Example: SHP1001"
            )

    # -------------------------------------------------
    # Mobile Number
    # -------------------------------------------------

    elif search_method == "Mobile Number":

        if not search_value.isdigit():

            return "Mobile number must contain only digits."

        if len(search_value) != 10:

            return "Mobile number must contain exactly 10 digits."

    # -------------------------------------------------
    # Email
    # -------------------------------------------------

    elif search_method == "Email":

        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

        if not re.fullmatch(pattern, search_value):

            return "Invalid email address."

    # -------------------------------------------------
    # Order ID
    # -------------------------------------------------

    elif search_method == "Order ID":

        if len(search_value.strip()) < 3:

            return "Invalid Order ID."

    # -------------------------------------------------
    # Customer Name
    # -------------------------------------------------

    elif search_method == "Customer Name":

        if len(search_value.strip()) < 3:

            return "Customer name must contain at least 3 characters."

    return None
