from nltk.stem import PorterStemmer  # type: ignore
from nltk.tokenize import LineTokenizer, WordPunctTokenizer  # type: ignore
from typing import List, Dict, Any, Tuple, Generator
import re
import string


__token_id: Dict[str, int] = {}
__nextId: int = 0
__stemmer: PorterStemmer = PorterStemmer()


class Token:
    def __init__(self, token: str, ID: int, position: Tuple[int, int], idx: int) -> None:
        self.txt: str = token
        self.ID: int = ID
        self.line: int = position[0]
        self.col: int = position[1]
        self.idx: int = idx

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

    if t_word not in __token_id:
        __token_id[t_word] = __nextId
        __nextId += 1

    return __token_id[t_word]


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

    # cleaning text from symbols and compressing whitespace only lines to empty lines
    inputString = re.sub('[{}]'.format(re.escape(string.punctuation)), ' ', inputString)
    inputString = '\n'.join(['' if line.isspace() else line for line in inputString.splitlines()])
    
    lines: Generator = LineTokenizer(blanklines='discard').span_tokenize(inputString)
    tk: List[str] = WordPunctTokenizer().tokenize(inputString)
    columns: Generator = WordPunctTokenizer().span_tokenize(inputString)
    
    tokens: List[str] = [token for token in tk]
    lin: List[Tuple[int, int]] = [span for span in lines]
    col: List[int] = [span[0] for span in columns]
      
    result: List[Token] = []
    line_id: int = 0
    line_offset: int = 0
    for idx, token in enumerate(tokens):
        if lin[line_id][1] < col[idx]:
            line_id += 1
            line_offset += lin[line_id][0] - lin[line_id - 1][1] - 1
        
        position: Tuple[int, int] = (line_id + line_offset + 1, col[idx] - lin[line_id][0] + 1)
        ID: int = process_token(token)
        result.append(Token(token, ID, position, idx))

    return result


def reset() -> None:
    global __token_id
    global __nextId

    __token_id = {}
    __nextId = 0
