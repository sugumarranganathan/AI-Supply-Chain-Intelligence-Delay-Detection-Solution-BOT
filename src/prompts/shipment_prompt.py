"""
Shipment Prompt
"""

SHIPMENT_PROMPT = """
Analyse the following shipment.

Shipment ID:
{shipment_id}

Origin:
{origin}

Destination:
{destination}

Current Status:
{status}

Provide:

1. Delay Analysis
2. Root Cause
3. Risk Level
4. Estimated Delay
5. Recommended Action
"""
