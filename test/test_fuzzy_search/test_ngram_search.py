import unittest
import inspect
import os

from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.NgramSearch import NgramSearch

class TestFragmentSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.test_directory = os.path.dirname(inspect.getfile(self.__class__))
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=True)
        self.searcher = NgramSearch(self.config)

    def test_no_duplicates(self):
        self.config.stop_words_file = os.path.join(self.test_directory, "../empty.txt")
        text_model = self.tokenizer.create_text_model(
            "There are few same parts, middle is just different and has nothing in common. part between beginning and the end is completely diverse, but the end is the same",
            self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(0, len(duplicates.cases))

    def test_strict_duplicates(self):
        text_model = self.tokenizer.create_text_model("All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.", self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_one_difference(self):
        text_model = self.tokenizer.create_text_model("Same1 part1 sentece1 same2 part2 sentece2 different same3 part3 sentece3 same4 part4 sentece4. Same1 part1 sentece1 Same2 part2 sentec2 absolutely Same3 part3 sentece3 Same4 part4 sentece4", self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_multiple_differences(self):
        self.config.ngram_n = 2
        text_model = self.tokenizer.create_text_model("Same1 part1 different same2 part2 sentece2 different same3 part3 sentece3 same4 part4 sentece4. Same1 part1 sentece1 Same2 part2 sentece2 absolutely Same3 part3 sentece3 Same4 different4 sentece4", self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_different_part(self):
        text_model = self.tokenizer.create_text_model("different different different same1 part1 sentece1 same2 part2 sentece2. absolutely absolutely absolutely same1 part1 sentece1 same2 part2 sentece2", self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_grouping(self):
        self.config.input_file = os.path.join(self.test_directory, "../text.txt")
        text_model = self.tokenizer.create_text_model_file(self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))
        self.assertEqual(31, duplicates.cases[0].text_fragments[1].length)
