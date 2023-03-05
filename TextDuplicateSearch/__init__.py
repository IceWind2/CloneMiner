from TextDuplicateSearch.DataModels.Configs.SearchConfig import SearchConfig
from TextDuplicateSearch.DuplicateSearch.StrictSearch.StrictDuplicates import StrictDuplicates
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.TextModel import TextModel
from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer

__classesFile: str = ''


def find_clones(config: SearchConfig) -> DuplicateCollection:
    tokenizer: Tokenizer = Tokenizer()
    tokens = tokenizer.tokenize_file(config)

    # for t in text_model.tokens:
    #     print(t.txt, '\n')

    result: DuplicateCollection = StrictDuplicates.get_duplicate_data(tokens, config)

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
