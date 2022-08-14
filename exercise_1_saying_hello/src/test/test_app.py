"""
Tests for saying hello app
"""
import sys

sys.path.append("src")  # pylint: disable=wrong-import-position
import io  # pylint: disable=wrong-import-position
import unittest  # pylint: disable=wrong-import-position

from rich import print  # pylint: disable=wrong-import-position
from rich.console import Console  # pylint: disable=wrong-import-position
from rich.prompt import Prompt  # pylint: disable=wrong-import-position

from greetings.greetings import (  # pylint: disable=wrong-import-position
    get_greeting,
    get_random_number,
)
from saying_hello_app import greet  # pylint: disable=wrong-import-position
from saying_hello_app import greet_different


class TestSayHello(unittest.TestCase):
    """
    Test suite
    """

    def setUp(self) -> None:
        # simulate console input
        input: str = ""
        console: Console = Console(file=io.StringIO())
        self.name: str = Prompt.ask(
            "What is your name",
            console=console,
            default="Josh",
            stream=io.StringIO(input),
        )
        self.output = console.file.getvalue()  # pylint: disable=no-member
        return super().setUp()

    def test_prompt_str_default(self) -> None:
        """
        Test the app runs without throwing any errors.
        """
        assert self.name == "Josh"
        expected = "What is your name (Josh): "
        print(repr(self.output))
        assert self.output == expected

    def test_greet(self) -> None:
        """
        Test greet function works
        """
        assert self.name == "Josh"
        greet(self.name)
        expected = ":rocket: Hello " + "Josh"
        self.assertEqual(greet(self.name), expected)

    def test_random_number(self) -> None:
        """
        Test random number generator is always returning 1,2, or 3
        """
        for _ in range(0, 500):
            self.assertIn(get_random_number(), [1, 2, 3])

    def test_get_greeting(self) -> None:
        """
        Test greeting function returns expected strings
        """
        for _ in range(0, 100):

            self.assertIn(
                get_greeting(get_random_number()),
                [":rocket: Hey, ", "Hello ", "Good morning :rocket: "],
            )

    def test_greet_different(self) -> None:
        """
        Test greeter can concat args properly
        """
        greeting: str = "How's it going, "
        name: str = "Glen"

        self.assertEqual(greet_different(greeting, name), "How's it going, Glen")

    def tearDown(self) -> None:
        return None
