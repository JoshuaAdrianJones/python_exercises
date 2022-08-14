"""
Saying hello app - get the users name and greet the user by name.
"""

from rich import print
from rich.prompt import Prompt

from greetings.greetings import (  # pylint: disable=import-error
    get_greeting,
    get_random_number,
)


def name_prompt() -> str:
    """Ask the user for their name"""
    return Prompt.ask("Please enter a your name")


def greet(name_prompt: str) -> str:
    """
    Append the users name to a greeting sentence.
    example usage: print(greet(name_prompt()))
    """
    return ":rocket: Hello " + name_prompt


def greet_different(greeting: str, name_prompt: str) -> str:
    """
    combine users name with a greeting
    """
    return greeting + name_prompt


if __name__ == "__main__":

    print(greet_different(get_greeting(get_random_number()), name_prompt()))
