# Create server parameters for stdio connection
import asyncio
import os

from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_mcp_adapters.tools import load_mcp_tools
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# server_params = StdioServerParameters(
#     command="python",
#     # Make sure to update to the full absolute path to your math_server.py file
#     args=["tools/math_server.py"],
# )

# llm = ChatOpenAI(
#     openai_api_key=api_key,
#     base_url="https://llm.dev.aicore.team/api",
#     model="deepseek-llama3-70b",
#     # model="llama3-8b",
# )
llm = ChatOpenAI(base_url="http://localhost:11434/v1", api_key="ollama", model="llama3.2:1b-instruct-q4_K_S",)


async def main():
    # async with stdio_client(server_params) as (read, write):
    #     async with ClientSession(read, write) as session:
    #         # Initialize the connection
    #         await session.initialize()

    #         # Get tools
    #         tools = await load_mcp_tools(session)

    #         # Create and run the agent
    #         agent = create_react_agent(llm, tools)
    #         agent_response = await agent.ainvoke({"messages": "what's (3 + 5) x 12?"})
    #         print(agent_response)

    async with MultiServerMCPClient(
        {
            "math": {
                # "command": "python",
                # Make sure to update to the full absolute path to your math_server.py file
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
            # "weather": {
            #     # make sure you start your weather server on port 8000
            #     "url": "http://localhost:8000/sse",
            #     "transport": "sse",
            # },
            # "command_line": {
            #     "command": "python",
            #     # Make sure to update to the full absolute path to your cli_server.py file
            #     "args": ["tools/cli_server.py"],
            #     "transport": "stdio",
            # },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
        math_response = await agent.ainvoke({"messages": "what's (4 + 5) x 12?"})
        # weather_response = await agent.ainvoke(
        #     {"messages": "what is the weather in nyc?"}
        # )
        # command_line_response = await agent.ainvoke(
        #     {"messages": "List all files and directories in the current directory."}
        # )
        print(math_response)
        # print(weather_response)
        # print(command_line_response)


if __name__ == "__main__":
    asyncio.run(main())
