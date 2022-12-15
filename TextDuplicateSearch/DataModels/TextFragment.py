from TextDuplicateSearch.TextProcessing.Tokenizer import Token


class TextFragment:
    def __init__(self, start: Token, end: Token, length: int) -> None:
        self.start: Token = start
        self.end: Token = end
        self.length: int = length
