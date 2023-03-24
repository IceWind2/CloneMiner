from __future__ import annotations
from typing import List

from TextDuplicateSearch.TextProcessing.Token import Token


class TextFragment:
    def __init__(self, token_list: List[Token]) -> None:
        self.tokens: List[Token] = token_list
        self._update_params()

    def _update_params(self) -> None:
        self.start: Token = self.tokens[0] if len(self.tokens) > 0 else Token.empty()
        self.end: Token = self.tokens[-1] if len(self.tokens) > 0 else Token.empty()
        self.length: int = len(self.tokens)
        self.idx = -1
        self.hash: int = 0

    def __str__(self) -> str:
        result: str = ''
        for i in range(len(self.tokens)):
            result += self.tokens[i].text + ' '

        return result

    def __repr__(self) -> str:
        result: str = ''
        for i in range(len(self.tokens)):
            result += self.tokens[i].text + ' '

        return result

    def merge_with(self, fragment: TextFragment) -> None:
        if self.start.idx == fragment.end.idx + 1:
            self.tokens = fragment.tokens + self.tokens
            self._update_params()
            return

        if self.end.idx + 1 == fragment.start.idx:
            self.tokens = self.tokens + fragment.tokens
            self._update_params()
            return

    def is_neighbor(self, fragment: TextFragment) -> bool:
        return self.start.idx == fragment.end.idx + 1 or self.end.idx + 1 == fragment.start.idx
