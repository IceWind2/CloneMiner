from typing import TextIO, List

from TextDuplicateSearch.StrictSearch import RepeatSearch
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.TextModel import TextModel

__classesFile: str = ''


def find_clones(inFile: str, minTokens: int, outFile: str) -> DuplicateCollection:
    text_model: TextModel = TextModel()
    text_model.build_from_file(inFile)
    for t in text_model.tokens:
        print(t.txt, '\n')

    result: DuplicateCollection = RepeatSearch.get_duplicate_data(text_model.tokens, minTokens)

    with open(outFile, 'w') as out:
        out.write(str(result))

    return result


def enable_token_classes(classesFile: str = 'TokenClasses.txt') -> None:
    global __classesFile

    __classesFile = classesFile


def disable_token_classes() -> None:
    global __classesFile

    __classesFile = ''
