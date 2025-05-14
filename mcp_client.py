import asyncio
import os

from dotenv import load_dotenv
from langchain_core.messages import AIMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

from langchain_aws import ChatBedrockConverse

llm = ChatBedrockConverse(model_id="amazon.nova-pro-v1:0", region_name="us-east-1")


async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
            "weather": {
                "url": "http://localhost:8080/sse",
                "transport": "sse",
            },
            "command_line": {
                "command": "python",
                "args": ["tools/cli_server.py"],
                "transport": "stdio",
            },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())

        math_response = await agent.ainvoke({"messages": "what's (4 + 5) x 12?"})
        final_answer = extract_final_answer(math_response)
        print(final_answer)

        weather_response = await agent.ainvoke(
            {"messages": "what is the weather in nyc?"}
        )
        final_answer = extract_final_answer(weather_response)
        print(final_answer)

        command_line_response = await agent.ainvoke(
            {"messages": "List all files and directories in the current directory."}
        )
        final_answer = extract_final_answer(command_line_response)
        print(final_answer)


def extract_final_answer(response):
    messages = response["messages"]
    final_answer = None
    for msg in reversed(messages):
        if isinstance(msg, AIMessage) and isinstance(msg.content, str):
            final_answer = msg.content
            break
    return final_answer


if __name__ == "__main__":
    asyncio.run(main())
