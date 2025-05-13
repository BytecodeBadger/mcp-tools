import requests
from bs4 import BeautifulSoup
from langchain.tools import BaseTool
from typing import Optional, Type

class WebScrapeTool(BaseTool):
    """Tool to scrape content from a website."""

    name:str = "website_scraper"
    description:str = "Scrapes the text content from a given URL.\n" \
                   "Useful for retrieving information from websites.\n" \
                   "Input to this tool should be a valid URL."

    def _run(self, url: str) -> str:
        """Scrape the content of the website at the given URL."""
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for bad status codes
            soup = BeautifulSoup(response.content, "html.parser")
            text_content = ' '.join(soup.stripped_strings)
            return text_content[:4096]  # Limit the output to avoid overwhelming the LLM
        except requests.exceptions.RequestException as e:
            return f"Error fetching URL '{url}': {e}"
        except Exception as e:
            return f"Error processing content from '{url}': {e}"

    async def _arun(self, url: str) -> str:
        """Asynchronous execution for web scraping."""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")
                text_content = ' '.join(soup.stripped_strings)
                return text_content[:4096]
        except httpx.RequestError as e:
            return f"Error fetching URL '{url}': {e}"
        except Exception as e:
            return f"Error processing content from '{url}': {e}"

if __name__ == '__main__':
    tool = WebScrapeTool()
    print(tool.run("https://en.wikipedia.org/wiki/Model_Context_Protocol"))