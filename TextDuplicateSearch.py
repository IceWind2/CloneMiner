import Tokenizer
import RepeatSearch
import os
from DuplicateData import DuplicateData
from typing import TextIO
from typing import List

__classesFile = ''


def find_clones(inFile: str, minTokens: int, outFile: str) -> None:
    text: TextIO = open(inFile, encoding='utf-8')
    tokens: List[Tokenizer.Token] = Tokenizer.tokenize(text.read(), __classesFile)
    
    result: DuplicateData = RepeatSearch.get_clone_data(tokens, minTokens)
    with open(outFile, 'w') as out:
        out.write(str(result))


def enable_token_classes(classesFile: str = os.path.join('lexer', 'TokenClasses.txt')) -> None:
    global __classesFile
    
    __classesFile = classesFile


def disable_token_classes() -> None:
    global __classesFile
    
    __classesFile = ''


if __name__ == '__main__':
    fin = "text.txt"
    fout = "res.txt"
    enable_token_classes()
    find_clones(fin, 3, fout)
