import subprocess
from typing import Optional, Type

from langchain.tools import BaseTool


class CommandLineTool(BaseTool):
    """Tool to execute shell commands."""

    name: str = "mac_command_executor"
    description: str = (
        "Executes commands on the local Mac operating system and returns the output.\n"
        "Use this tool to interact with the file system, run system utilities, and more.\n"
        "Input to this tool should be a valid shell command."
    )

    def _run(self, query: str) -> str:
        """Execute the command and return the output."""
        try:
            process = subprocess.run(
                query, shell=True, capture_output=True, text=True, check=False
            )
            if process.returncode == 0:
                return process.stdout.strip()
            else:
                return f"Command failed with error: {process.stderr.strip()}"
        except Exception as e:
            return f"Error executing command: {e}"

    async def _arun(self, query: str) -> str:
        """Asynchronous execution is not directly supported for subprocess."""
        raise NotImplementedError(
            "Asynchronous execution is not supported for this tool."
        )


if __name__ == "__main__":
    tool = CommandLineTool()
    print(tool.run("ls -l"))
    print(tool.run("pwd"))
    print(tool.run("cat LICENSE"))
