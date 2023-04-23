"""
Saying hello app - get the users name and greet the user by name.
"""

from greetings import greetings  # type: ignore
from rich import print
from rich.prompt import Prompt


def name_prompt() -> str:
    """Ask the user for their name"""
    return Prompt.ask("Please enter your name")


if __name__ == "__main__":
    print(greetings.add_name_to_greeting(greetings.greeting_generator(), name_prompt()))
