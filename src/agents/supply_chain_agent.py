"""
Supply Chain Agent
"""

from langchain.agents import create_react_agent
from langchain import hub

from src.models.llm import LLMFactory
from src.tools import TOOLS


def create_supply_chain_agent():
    """
    Create a ReAct agent with all registered tools.
    """

    llm = LLMFactory.create()

    prompt = hub.pull("hwchase17/react")

    return create_react_agent(
        llm=llm,
        tools=TOOLS,
        prompt=prompt,
    )
