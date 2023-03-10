from typing import TextIO, List

from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.TextProcessing.Token import Token


class TextModel:
    def __init__(self, tokens: List[Token]) -> None:
        self.text: str = ""
        self.tokens: List[Token] = tokens
        self.parts: List[TextFragment] = []

    def split_into_parts(self, part_len: int) -> None:
        num: int = len(self.tokens) // part_len if len(self.tokens) % part_len == 0 else len(self.tokens) // part_len + 1

        for i in range(0, num - 1):
            self.parts.append(TextFragment(self.tokens[i * part_len: (i + 1) * part_len]))

        self.parts.append(TextFragment(self.tokens[(num - 1) * part_len: None]))
