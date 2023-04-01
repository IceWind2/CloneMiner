from typing import List, Type

from TextDuplicateSearch.DataModels.DuplicateCollection import DuplicateCollection
from TextDuplicateSearch.DataModels.TextModel import TextModel
from TextDuplicateSearch.DuplicateSearch.DuplicateSearcher import DuplicateSearcher
from TextDuplicateSearch.DuplicateSearch.StrictSearch.SuffixSearch import SuffixSearch
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.FragmentSearch import FragmentSearch
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.NgramSearch import NgramSearch
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.TextProcessing.Token import Token
from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer

strict_searchers: List[Type[DuplicateSearcher]] = [SuffixSearch]
fuzzy_searchers: List[Type[DuplicateSearcher]] = [FragmentSearch, NgramSearch]


def strict_search(config: SearchConfig, text: str = "") -> DuplicateCollection:
    config.need_text_processing = False

    text_model: TextModel = process_text(config, text)

    searcher: DuplicateSearcher = strict_searchers[config.searcher_type](config)

    duplicates: DuplicateCollection = searcher.find_duplicates(text_model)
    if config.output_file:
        duplicates.output(config.output_file)

    return duplicates


def fuzzy_search(config: SearchConfig, text: str = "") -> DuplicateCollection:
    text_model: TextModel = process_text(config, text)

    searcher: DuplicateSearcher = fuzzy_searchers[config.searcher_type](config)

    duplicates: DuplicateCollection = searcher.find_duplicates(text_model)
    if config.output_file:
        duplicates.output(config.output_file)

    return duplicates


def process_text(config: SearchConfig, text: str = "") -> TextModel:
    tokenizer: Tokenizer = Tokenizer()

    if not text:
        return tokenizer.create_text_model_file(config)
    else:
        return tokenizer.create_text_model(text, config)


def create_config() -> SearchConfig:
    return SearchConfig()
