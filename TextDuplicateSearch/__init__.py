from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.FragmentSearch import FragmentSearch
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.NgramSearch import NgramSearch
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.Tools.EditDistance import EditDistance
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.Tools.Hashing import Hashing
from TextDuplicateSearch.DuplicateSearch.StrictSearch.StrictDuplicates import StrictDuplicates
from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.TextModel import TextModel
from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer

__classesFile: str = ''


def find_clones(config: SearchConfig) -> DuplicateCollection:
    tokenizer: Tokenizer = Tokenizer()
    tokens = tokenizer.tokenize_file(config)
    tm = TextModel(tokens)
    # for t in text_model.tokens:
    #     print(t.txt, '\n')

    # result: DuplicateCollection = StrictDuplicates.get_duplicate_data(tokens, config)

    fs = FragmentSearch(Hashing.signature_hash_func, EditDistance.ukkonen_asm, config)
    # fs = NgramSearch(config)
    result = fs.find_duplicates(tm)

    # with open(config.output_file, 'w') as out:
    #     out.write(str(result))

    return result
