from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

root_agent = Agent(
    name="tool_agent",
    model  = "gemini-2.5-flash-lite",
    description="Tool agent",
    instruction="""
    your are an intelligent agent can summarize the content of the book title is given to you.
     also provide the online link to buy that particular book ,use the provided tools -google_search.
    """,
    tools=[google_search],
)
