import inspect
import os
import unittest

from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer


class TestTokenizer(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.test_directory = os.path.dirname(inspect.getfile(self.__class__))
        self.config = SearchConfig(input_file=os.path.join(self.test_directory, "../text.txt"),
                                   output_file="",
                                   min_dup_length=3)

    def test_empty(self):
        tokens = self.tokenizer.tokenize("", self.config)
        self.assertEqual(0, len(tokens))

    def test_one_word(self):
        tokens = self.tokenizer.tokenize("one", self.config)
        self.assertEqual("one", tokens[0].text)
        self.assertEqual(2, tokens[0].id)

    def test_multiple_words(self):
        tokens = self.tokenizer.tokenize("one two three\nfour", self.config)
        self.assertEqual(4, len(tokens))

    def test_multiple_lines(self):
        tokens = self.tokenizer.tokenize("one\n two three\nfour", self.config)
        self.assertEqual(3, tokens[3].line)

    def test_filter(self):
        tokens = self.tokenizer.tokenize("one        two  three,\t four", self.config)
        self.assertEqual(12, tokens[1].col)
        self.assertEqual("three", tokens[2].text)
        self.assertEqual("four", tokens[3].text)

    def test_tokenize_file(self):
        tokens = self.tokenizer.tokenize_file(self.config)
        self.assertEqual(3619, len(tokens))
        self.assertEqual("noachian", tokens[0].processed)
        self.assertEqual(2, tokens[0].id)

    def test_stop_words(self):
        tokens = self.tokenizer.tokenize("the a is this", self.config)
        self.assertEqual(0, len(tokens))

    def test_stop_words_file(self):
        self.config.stop_words_file = os.path.join(self.test_directory, "../text.txt")
        tokens = self.tokenizer.tokenize("the a is this", self.config)
        self.assertEqual(4, len(tokens))


if __name__ == '__main__':
    unittest.main()
