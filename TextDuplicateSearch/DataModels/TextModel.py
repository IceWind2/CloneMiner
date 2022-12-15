from typing import TextIO, List

import TextDuplicateSearch.TextProcessing.Tokenizer as Tokenizer


class TextModel:
    def __init__(self) -> None:
        self.text: str = ""
        self.tokens = []

    def build_from_file(self, file_name: str) -> None:
        input_file: TextIO = open(file_name, encoding='utf-8')
        self.text: str = input_file.read()
        self.tokens = Tokenizer.tokenize(self.text, "")
        input_file.close()

    def build_from_string(self, text: str):
        self.text = text
        self.tokens = Tokenizer.tokenize(self.text, "")
