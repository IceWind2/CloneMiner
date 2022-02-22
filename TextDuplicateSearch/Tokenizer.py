import antlr4  # type: ignore
from nltk.stem import PorterStemmer  # type: ignore
from typing import List, Dict, Any
import re

from TextDuplicateSearch.lexer import MyGrammarLexer  # type: ignore


token_id: Dict[str, int] = {}
__nextId: int = 0
__stemmer: PorterStemmer = PorterStemmer()


class Token:
    def __init__(self, token: antlr4.Token, ID: int, position: int) -> None:
        self.raw = token
        self.txt: str = token.text
        self.ID: int = ID
        self.pos: int = position

    def __str__(self) -> str:
        return self.txt

    def __repr__(self) -> str:
        return f'{self.txt}:{self.ID}'

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Token):
            return self.ID == other.ID
        return False


def process_token(text: str) -> int:
    global __nextId

    t_word: str = __stemmer.stem(text.lower())

    if t_word not in token_id:
        token_id[t_word] = __nextId
        __nextId += 1

    return token_id[t_word]


def tokenize(inputString: str, classesFile: str) -> List[Token]:
    if classesFile != '':
        try:
            with open(classesFile, 'r') as tc:
                classes: List[str] = re.sub('\n+', '', tc.read()).split(';')[:-1]

            for cls in classes:
                line: str = re.sub("[\s\t]+", ' ', cls)
                for word in line.split():
                    process_token(word)

        except Exception:
            print("Token classes file not found.")

    data = antlr4.InputStream(inputString)
    lexer = MyGrammarLexer.MyGrammarLexer(data)
    tokens = lexer.getAllTokens()
    result: List[Token] = []

    for pos, token in enumerate(tokens):
        ID: int = process_token(token.text)
        result.append(Token(token, ID, pos))

    return result
