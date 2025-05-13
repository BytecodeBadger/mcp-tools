# math_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    with open("math_server.log", "a") as f:
        print(f"***********************Adding numbers: {a}, {b}", file=f)
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    with open("math_server.log", "a") as f:
        print(f"***********************Multiplying numbers: {a}, {b}", file=f)
    return a * b


if __name__ == "__main__":
    mcp.run(transport="sse")
    # mcp.run(transport="stdio")
