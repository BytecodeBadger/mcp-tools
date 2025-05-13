import os

from dotenv import load_dotenv  
from langchain.agents import AgentType, initialize_agent
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

from tools.cli_tool import CommandLineTool
from tools.web_scrape_tool import WebScrapeTool

# Load OpenAI API key from environment variables
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("Please set your OPENAI_API_KEY environment variable.")

def main():
    llm = ChatOpenAI(
        base_url="https://llm.dev.aicore.team/api", 
        api_key=api_key, 
        model="llama3-8b", 
    )
    # Load the custom tools
    cli_tool = CommandLineTool()
    web_scrape_tool = WebScrapeTool()
    tools = [cli_tool, web_scrape_tool]

    # Initialize the agent
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # interactions
    print("Agent interacting with the command line:")
    agent.invoke("List all files and directories in the current directory.")

    print("\nAgent scraping a website:")
    agent.run("What is the title of the website at https://www.wikipedia.org/?")


if __name__ == "__main__":
    main()
