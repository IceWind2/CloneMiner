from TextDuplicateSearch.TextProcessing.Token import Token


class TextFragment:
    def __init__(self, start: Token, end: Token) -> None:
        self.start: Token = start
        self.end: Token = end
        self.length: int = end.idx - start.idx + 1

