from typing import TextIO, List

from TextDuplicateSearch.TextProcessing.Token import Token


class TextModel:
    def __init__(self, tokens: List[Token]) -> None:
        self.text: str = ""
        self.tokens: List[Token] = tokens
