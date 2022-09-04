"""
Tests for character count
"""
import io
import unittest

from rich import print
from rich.console import Console
from rich.prompt import Prompt


class TestCounting(unittest.TestCase):
    """
    Test suite
    """

    def setUp(self) -> None:
        # simulate console input
        input: str = "homer"
        console: Console = Console(file=io.StringIO())
        self.text: str = Prompt.ask(
            "Enter some text",
            console=console,
            default="homer",
            stream=io.StringIO(input),
        )
        # pylint: disable-next=no-member
        self.output = console.file.getvalue()  # type: ignore
        return super().setUp()

    def test_prompt_str_default(self) -> None:
        """
        Test the app runs without throwing any errors.
        """
        assert self.text == "homer"
        expected: int = 5
        print(repr(self.output))
        assert len(self.text) == expected

    def tearDown(self) -> None:
        return None
