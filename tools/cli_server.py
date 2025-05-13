import subprocess
from typing import Optional, Type

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CommandLineTool")


@mcp.tool()
def execute_command(command: str) -> str:
    """Execute a cli shell command and return the output."""
    try:
        process = subprocess.run(
            command, shell=True, capture_output=True, text=True, check=False
        )
        if process.returncode == 0:
            return process.stdout.strip()
        else:
            return f"Command failed with error: {process.stderr.strip()}"
    except Exception as e:
        return f"Error executing command: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
