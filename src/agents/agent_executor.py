"""
Agent Executor
"""

from langchain.agents import AgentExecutor

from src.agents.supply_chain_agent import create_supply_chain_agent
from src.tools import TOOLS


def create_agent_executor():
    """
    Create an executable agent.
    """

    agent = create_supply_chain_agent()

    return AgentExecutor(
        agent=agent,
        tools=TOOLS,
        verbose=True,
    )
