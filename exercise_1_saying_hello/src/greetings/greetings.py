"""
Provide a method to generate random greetings
"""
import random


def get_random_number() -> int:
    """get a random number between 0 and 10"""
    return random.randint(1, 3)


def get_greeting(rand: int) -> str:
    """
    Given an integer return a greeting string.
    """
    match rand:
        case 1:
            return ":rocket: Hey, "
        case 2:
            return "Hello "
        case 3:
            return "Good morning :rocket: "
