from typing import List

from TextDuplicateSearch.TextProcessing.Token import Token


class TextFragment:
    def __init__(self, token_list: List[Token]) -> None:
        self.tokens = token_list
        self.start = token_list[0]
        self.end = token_list[-1]
        self.length: int = len(self.tokens)

        self.hash: int = 0
