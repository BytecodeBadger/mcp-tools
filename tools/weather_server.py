from typing import List

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Use the weather tool to answer: what is the weather in nyc?"""
    return "It's always sunny in New York"


if __name__ == "__main__":
    mcp.run(transport="sse")
