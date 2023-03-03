import re
import string

from nltk.stem import PorterStemmer  # type: ignore
from nltk.tokenize import LineTokenizer, WordPunctTokenizer  # type: ignore
from typing import List, Dict, Tuple, Generator, TextIO

from TextDuplicateSearch.TextProcessing.Token import Token
from TextDuplicateSearch.DataModels.Configs.SearchConfig import SearchConfig


class Tokenizer:
    def __init__(self):
        self.token_id: Dict[str, int] = {}
        self.next_id: int = 0
        self.stemmer: PorterStemmer = PorterStemmer()

    def tokenize_file(self, search_config: SearchConfig) -> List[Token]:
        input_file: TextIO = open(search_config.input_file, encoding=search_config.file_encoding)
        text: str = input_file.read()
        input_file.close()
        return self.tokenize(text, search_config)

    def tokenize(self, input_string: str, search_config) -> List[Token]:
        # if classes_file != '':
        #     try:
        #         with open(classes_file, 'r') as tc:
        #             classes: List[str] = re.sub('\n+', '', tc.read()).split(';')[:-1]
        #
        #         for cls in classes:
        #             line: str = re.sub("[\s\t]+", ' ', cls)
        #             for word in line.split():
        #                 self._process_token(word)
        #
        #     except Exception:
        #         print("Token classes file not found.")

        # cleaning text from symbols and compressing whitespace only lines to empty lines
        input_string = re.sub('[{}]'.format(re.escape(string.punctuation)), ' ', input_string)
        input_string = '\n'.join(['' if line.isspace() else line for line in input_string.splitlines()])

        lines: Generator = LineTokenizer(blanklines='discard').span_tokenize(input_string)
        tk: List[str] = WordPunctTokenizer().tokenize(input_string)
        columns: Generator = WordPunctTokenizer().span_tokenize(input_string)

        tokens: List[str] = [token for token in tk]
        row: List[Tuple[int, int]] = [span for span in lines]
        col: List[int] = [span[0] for span in columns]

        # calculating token coordinates in text
        result: List[Token] = []
        line_id: int = 0
        line_offset: int = 0
        for idx, token in enumerate(tokens):
            if row[line_id][1] < col[idx]:
                line_id += 1
                line_offset += row[line_id][0] - row[line_id - 1][1] - 1

            position: Tuple[int, int] = (line_id + line_offset + 1, col[idx] - row[line_id][0] + 1)
            ID: int = self._get_token_id(token, search_config.need_text_processing)
            result.append(Token(token, ID, position, idx))

        return result

    def reset(self) -> None:
        self.token_id = {}
        self.next_id = 0

    def _get_token_id(self, text: str, need_processing) -> int:
        token = text

        if need_processing:
            token = self._process_text(token)

        if token not in self.token_id:
            self.token_id[token] = self.next_id
            self.next_id += 1

        return self.token_id[token]

    def _process_text(self, text: str) -> str:
        token: str = self.stemmer.stem(text.lower())
        return token

