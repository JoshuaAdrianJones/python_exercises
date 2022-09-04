"""
Provide a method to generate random greetings
"""
import random


def get_random_number() -> int:
    """
    Get a random number between 0 and 10
    """
    return random.randint(1, 3)


def select_greeting(number: int) -> str:
    """
    Given an integer return a greeting string.
    """
    response: str
    match number:
        case 1:
            response = ":rocket: Hey, "
        case 2:
            response = "Hello "
        case 3:
            response = "Good morning :rocket: "
        case _:
            raise ValueError("Invalid number provided to greeting selector")
    return response


def greeting_generator():
    """
    combine number and selector to generate a greeting
    """
    return select_greeting(get_random_number())


def add_name_to_greeting(greeting: str, name_prompt: str) -> str:
    """
    combine users name with a greeting
    """
    return greeting + name_prompt
