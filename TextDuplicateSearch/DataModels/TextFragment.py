from typing import List

from TextDuplicateSearch.TextProcessing.Token import Token


class TextFragment:
    def __init__(self, token_list: List[Token]) -> None:
        self.tokens: List[Token] = token_list
        self.start: Token = token_list[0] if len(token_list) > 0 else Token.empty()
        self.end: Token = token_list[-1] if len(token_list) > 0 else Token.empty()
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

