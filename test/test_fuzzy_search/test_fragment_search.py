import inspect
import os
import unittest

from TextDuplicateSearch import Tokenizer, SearchConfig, TextModel, FragmentSearch, Hashing, EditDistance


class TestFragmentSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.test_directory = os.path.dirname(inspect.getfile(self.__class__))
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=True)
        self.searcher = FragmentSearch(Hashing.signature_hash_func,
                                       EditDistance.ukkonen_asm,
                                       self.config)

    def test_strict_duplicates(self):
        text_model = self.tokenizer.create_text_model("All work and no play makes Jack a dull boy. All work and no play makes Jack a dull boy.", self.config)
        self.searcher.config.fragment_size = 6
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_one_difference(self):
        text_model = self.tokenizer.create_text_model("Just an identical part of a bit different small phrases. Just an identical part of absolutely same small phrases.", self.config)
        self.searcher.config.fragment_size = 6
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_one_case_1(self):
        text_model = self.tokenizer.create_text_model("Two paragraphs with two different parts in text. Two phrases with few different parts of text", self.config)
        self.searcher.config.fragment_size = 6
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_one_case_2(self):
        text_model = self.tokenizer.create_text_model("Two a bit different paragraphs. Algorithm should recognize this phrases as a clone. Two a little different paragraphs. Algorithm can recognize that this phrases as a clone", self.config)
        self.searcher.config.fragment_size = 8
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_multiple_cases(self):
        self.config.stop_words_file = os.path.join(self.test_directory, "../empty.txt")
        text_model = self.tokenizer.create_text_model("There are few same parts, middle is just different and has nothing in common, but the end is the same. There are few same parts, part between beginning and the end is completely diverse, but the end is the same", self.config)
        self.searcher.config.fragment_size = 5
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(2, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))

    def test_grouping(self):
        self.config.input_file = os.path.join(self.test_directory, "../text.txt")
        self.config.fragment_size = 7
        text_model = self.tokenizer.create_text_model_file(self.config)
        duplicates = self.searcher.find_duplicates(text_model)
        self.assertEqual(1, len(duplicates.cases))
        self.assertEqual(2, len(duplicates.cases[0].text_fragments))
        self.assertEqual(28, duplicates.cases[0].text_fragments[1].length)


if __name__ == '__main__':
    unittest.main()
