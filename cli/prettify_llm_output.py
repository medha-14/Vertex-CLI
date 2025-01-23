from rich import print
from rich.console import Console
from rich.markdown import Markdown


def prettify_llm_output(response):
    """
    Prettifies the output from a language model response by stripping leading 
    and trailing whitespace and code block markers, then prints it as Markdown 
    to the console.

    Args:
        response (str): The raw response from the language model.

    Returns:
        None
    """
    markdown_output = response.strip().strip("```")
    console = Console()
    md = Markdown(markdown_output)
    print()
    console.print(md)
    print()
