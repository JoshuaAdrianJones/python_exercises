"""
Tests for saying hello app
"""
import io
import unittest

from greetings import greetings  # type: ignore
from rich import print
from rich.console import Console
from rich.prompt import Prompt


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
        # pylint: disable-next=no-member
        self.output = console.file.getvalue()  # type: ignore
        return super().setUp()

    def test_prompt_str_default(self) -> None:
        """
        Test the app runs without throwing any errors.
        """
        assert self.name == "Josh"
        expected = "What is your name (Josh): "
        print(repr(self.output))
        assert self.output == expected

    def test_random_number(self) -> None:
        """
        Test random number generator is always returning 1,2, or 3
        """
        for _ in range(0, 500):
            self.assertIn(greetings.get_random_number(), [1, 2, 3])

    def test_get_greeting(self) -> None:
        """
        Test greeting function returns expected strings
        """
        for _ in range(0, 100):
            self.assertIn(
                greetings.select_greeting(greetings.get_random_number()),
                [":rocket: Hey, ", "Hello ", "Good morning :rocket: "],
            )

    def test_add_name_to_greeting(self) -> None:
        """
        Test greeter can concat args properly
        """
        greeting: str = "How's it going, "
        name: str = "Glen"

        self.assertEqual(
            greetings.add_name_to_greeting(greeting, name), "How's it going, Glen"
        )

    def tearDown(self) -> None:
        return None
