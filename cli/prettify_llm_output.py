from rich import print
from rich.console import Console
from rich.markdown import Markdown


def prettify_llm_output(response):
    markdown_output = response.strip().strip("```")
    console = Console()
    md = Markdown(markdown_output)
    console.print(md)
