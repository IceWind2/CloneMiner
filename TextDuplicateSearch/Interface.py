from typing import TextIO, List

from TextDuplicateSearch import RepeatSearch
from TextDuplicateSearch import Tokenizer
from TextDuplicateSearch.DuplicateData import DuplicateData


__classesFile: str = ''


def find_clones(inFile: str, minTokens: int, outFile: str) -> None:
    text: TextIO = open(inFile, encoding='utf-8')
    tokens: List[Tokenizer.Token] = Tokenizer.tokenize(text.read(), __classesFile)

    result: DuplicateData = RepeatSearch.get_clone_data(tokens, minTokens)
    with open(outFile, 'w') as out:
        out.write(str(result))


def enable_token_classes(classesFile: str = 'TokenClasses.txt') -> None:
    global __classesFile

    __classesFile = classesFile


def disable_token_classes() -> None:
    global __classesFile

    __classesFile = ''
