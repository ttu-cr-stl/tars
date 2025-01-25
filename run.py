"""
This pipeline recommends the best location for an event.
Uses laserfocus API to fetch events and favorite locations.

Built with LangChain.

Works with any LLM API that supports tool calling.
"""

import time

from langchain_ollama import ChatOllama

from langchain_core.messages import HumanMessage, SystemMessage

import os

from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

from src.utils.logger import logger

context_window = [
    SystemMessage(content="You are a helpful assistant that asks the user for their name until they give it to you and when the user answers 'Andres' you will respond with 'Hello Andres!' and be finished."),
    HumanMessage(content="Hello there!")
]

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    logger.info(f"Multiplying {a} and {b}")
    return a * b

@tool
def ask_user(question: str) -> str:
    """Ask the user a question."""
    logger.info(f"Asking user: {question}")
    user_input = input(question)
    message = HumanMessage(content=user_input)
    context_window.append(message)
    return user_input

logger.info("Initializing model...")

model = ChatOllama(
    model="llama3.2:latest",
    temperature=0.5,
    base_url=os.getenv('OLLAMA_API_URL')
)

tools = [
    ask_user,
    multiply
]

agent = create_react_agent(model, tools)

logger.success("Model initialized.")

logger.info("Invoking agent...")

for chunk in agent.stream(
    {"messages": context_window},
    {"recursion_limit": 100}
):
    print(chunk)
    print("----")
