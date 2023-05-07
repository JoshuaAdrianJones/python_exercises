"""
Saying a random quote
"""
import json
from dataclasses import dataclass
from pathlib import PosixPath
from random import choice
from typing import Literal, Optional, Union

source_names = [Literal["qod"], Literal["type_fit"], Literal["zen"]]
sources = {
    "qod": PosixPath("./test/fixtures/quotes.rest.qod.json"),
    "type_fit": PosixPath("./test/fixtures/type_fit_quotes.json"),
    "zen": PosixPath("./test/fixtures/zen_quotes_random.json"),
}
selected_source = choice(list(sources.keys()))


@dataclass
class Quote:
    """stores quote data"""

    quote: str
    author: str


@dataclass
class QuoteList:
    """Store the quotes and keep track of which source it came from"""

    quotes: list[Quote]
    source: Literal["qod", "type_fit", "zen"]


def get_source_path(sources: dict[str, PosixPath], selected_source: str) -> PosixPath:
    """given a source name return the path to that source"""
    return sources[selected_source]


def parse_qod(path: PosixPath) -> QuoteList:
    """read qod type json files"""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
        quotes = data["contents"]["quotes"]

        return QuoteList(
            [Quote(quote["quote"], str(quote["author"])) for quote in quotes],
            "qod",
        )


def parse_type_fit(path: PosixPath) -> QuoteList:
    """read type_fit type json files"""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
        return QuoteList(
            [Quote(quote["text"], str(quote["author"])) for quote in data],
            "type_fit",
        )


def parse_zen(path: PosixPath) -> QuoteList:
    """read type_fit type json files"""
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
        quotes = data["quotes"]
        return QuoteList(
            [Quote(quote["q"], str(quote["a"] if not None else "")) for quote in quotes],
            "zen",
        )


def load_quotes_from_source(
    path: PosixPath, selected_source: str
) -> Union[QuoteList, None]:
    """
    read the quotes from a json file
    """
    if selected_source == "qod":
        return parse_qod(path)
    if selected_source == "zen":
        return parse_zen(path)
    if selected_source == "type_fit":
        return parse_type_fit(path)
    return None


def get_quote(quote_list: Optional[QuoteList]) -> Quote:
    """
    return a random quote from source, picking a source at random
    Returns:
    """
    if isinstance(quote_list, QuoteList):
        choice(quote_list.quotes)
        return choice(quote_list.quotes)

    return Quote("default", "default")


if __name__ == "__main__":
    print("welcome to random quote generator")
    print("getting quotes...")
    source = sources[selected_source]
    print(source)
    quote_list = load_quotes_from_source(source, selected_source)
    print("The quote is:")
    print('"' + get_quote(quote_list).quote + '"')
    print("and it was said by " + get_quote(quote_list).author)
