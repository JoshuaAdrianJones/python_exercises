"""
Tests for saying hello app
"""
import unittest
from pathlib import PosixPath

from quote_api import Quote, get_source_path, parse_qod, parse_type_fit, parse_zen


class TestGetQuote(unittest.TestCase):
    """
    Test suite
    """

    def setUp(self) -> None:
        self.qod = PosixPath("./src/test/fixtures/quotes.rest.qod.json")
        self.type_fit = PosixPath("./src/test/fixtures/type_fit_quotes.json")
        self.zen = PosixPath("./src/test/fixtures/zen_quotes_random.json")
        self.sources = {
            "qod": self.qod,
            "type_fit": self.type_fit,
            "zen": self.zen,
        }

    def test_can_make_quote_objects(self) -> None:
        """check quote object works as intended"""
        random_quote = Quote("this is a random quote", "Josh")
        assert random_quote.quote == "this is a random quote"
        assert random_quote.author == "Josh"

    def test_select_source(self) -> None:
        """check that selecting the source returns a path"""
        example_valid_source_name = "zen"
        source = get_source_path(self.sources, example_valid_source_name)
        self.assertEqual(type(source), PosixPath)


class TestJSONLoader(unittest.TestCase):
    """
    make sure we can load Json correctly
    """

    def setUp(self) -> None:
        self.qod = PosixPath("./src/test/fixtures/quotes.rest.qod.json")
        self.type_fit = PosixPath("./src/test/fixtures/type_fit_quotes.json")
        self.zen = PosixPath("./src/test/fixtures/zen_quotes_random.json")

    def test_can_load_qod_source(self) -> None:
        "check qod files can be read correctly"
        self.assertEqual(
            parse_qod(self.qod).quotes[0].quote,
            "Logic will get you from A to B. Imagination will take you everywhere.",
        )

    def test_can_load_type_fit_source(self) -> None:
        "check type_fit iles can be read correctly"
        self.assertEqual(
            parse_type_fit(self.type_fit).quotes[0].quote,
            "Genius is one percent inspiration and ninety-nine percent perspiration.",
        )

    def test_can_load_zen_source(self) -> None:
        "check zen files can be read correctly"
        self.assertEqual(
            parse_zen(self.zen).quotes[0].quote,
            "Try not to become a man of success, but rather try to become a man of value.",
        )
