from typing import List

from TextDuplicateSearch.TextProcessing.Token import Token


class TextFragment:
    def __init__(self, token_list: List[Token]) -> None:
        self.tokens: List[Token] = token_list
        self.start: Token = token_list[0] if len(token_list) > 0 else None
        self.end: Token = token_list[-1] if len(token_list) > 0 else None
        self.length: int = len(self.tokens)

        self.hash: int = 0
