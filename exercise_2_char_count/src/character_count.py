"""
count the number of characters: prompts for a string (word or a string)
and return the length of the string.
"""

from rich import print
from rich.prompt import Prompt


def text_prompt() -> str:
    """Ask the user for some text"""
    return Prompt.ask("Please enter some text")


def input_handler() -> str:
    """
    Loop until the user provides a valid input
    """
    while True:
        try:
            user_input: str = text_prompt()
            if user_input:
                return user_input

            raise ValueError("Input must not be none")

        except ValueError as empty_input_msg:
            print(empty_input_msg)


if __name__ == "__main__":
    input: str = input_handler()
    print(f"{input} has {len(input)} characters")
