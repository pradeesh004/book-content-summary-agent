# book-content-summary-agent
📘 Book Summary Tool Agent

This project demonstrates how to create an intelligent agent using Google ADK that can summarize a book based on its title and provide an online purchase link for the book using Google Search.

🚀 Features

Accepts a book title as input

Generates a concise summary of the book

Searches the web to find an online link to buy the book

Uses Google ADK Agent framework

Integrates Google Search tool for real-time results

🧠 How It Works

An Agent is created using the Gemini 2.5 Flash Lite model.

The agent is instructed to:

Summarize the given book

Find an online purchase link

The google_search tool is used to fetch reliable buying options.

📂 Code Overview
from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.5-flash-lite",
    description="Tool agent",
    instruction="""
    you are an intelligent agent that summarizes a given book title
    and provides an online link to buy that book using google_search.
    """,
    tools=[google_search],
)

🛠 Requirements

Python 3.8+

Google ADK installed

Access to Gemini models

Internet connection (for Google Search)

▶️ Usage

Provide a book title as input to the agent

The agent will:

Generate a book summary

Return an online link where the book can be purchased

📌 Example Use Case

Students looking for quick book summaries

Readers deciding whether to buy a book

Educational or recommendation systems

📄 Notes

Ensure API access and permissions are properly configured.

Search results depend on real-time Google Search availability.

✨ Author

Developed as a simple example of tool-enabled AI agents using Google ADK.
