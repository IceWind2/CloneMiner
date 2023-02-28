from typing import TextIO, List

from TextDuplicateSearch.DataModels.Configs.SearchConfig import SearchConfig
from TextDuplicateSearch.StrictSearch import RepeatSearch
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.TextModel import TextModel

__classesFile: str = ''


def find_clones(config: SearchConfig) -> DuplicateCollection:
    text_model: TextModel = TextModel()
    text_model.build_from_file(config.input_file)
    # for t in text_model.tokens:
    #     print(t.txt, '\n')

    result: DuplicateCollection = RepeatSearch.get_duplicate_data(text_model.tokens, config.min_dup_length)

    with open(config.output_file, 'w') as out:
        out.write(str(result))

    return result


# def enable_token_classes(classesFile: str = 'TokenClasses.txt') -> None:
#     global __classesFile
#
#     __classesFile = classesFile
#
#
# def disable_token_classes() -> None:
#     global __classesFile
#
#     __classesFile = ''
