"""
count the number of characters: prompts for a string (word or a string)
and return the length of the string.
"""

from rich import print
from rich.prompt import Prompt


def text_prompt() -> str:
    """Ask the user for some text"""
    return Prompt.ask("Please enter some text")


if __name__ == "__main__":
    input: str = text_prompt()
    print(f"{input} has {len(input)} characters")
