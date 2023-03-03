import unittest

from TextDuplicateSearch.DataModels.Configs.SearchConfig import SearchConfig
from TextDuplicateSearch.StrictSearch.SuffixArray import build_from_array
from TextDuplicateSearch.StrictSearch.SuffixArray import build_from_tokens
from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer


class UnitSuffixArray(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()

    def test_empty(self):
        test_array = []
        suf_array, _ = build_from_array(test_array)
        self.assertEqual(0, len(suf_array))

    def test_one_word(self):
        test_array = [0]
        suf_array, _ = build_from_array(test_array)
        self.assertEqual(1, len(suf_array))
        self.assertEqual(0, suf_array[0])

    def test_two_equal_words(self):
        test_array = [1, 2, 3, 4, 2, 5]
        suf_array, _ = build_from_array(test_array)
        self.assertEqual(1, suf_array[1])
        self.assertEqual(4, suf_array[2])

    def test_lcp_format(self):
        test_array = [1, 2, 3, 4, 2, 5]
        suf_array, lcp_array = build_from_array(test_array)
        self.assertEqual(-1, lcp_array[0])

    def test_lcp(self):
        test_array = [1, 2, 3, 4, 2, 5]
        suf_array, lcp_array = build_from_array(test_array)
        self.assertEqual(1, lcp_array[2])


class IntegrationSuffixArray(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   min_dup_length=3)

    def test_empty(self):
        tokens = self.tokenizer.tokenize("", self.config)
        suf_array, lcp_array = build_from_tokens(tokens)
        self.assertEqual(0, len(suf_array))

    def test_one_word(self):
        tokens = self.tokenizer.tokenize("one", self.config)
        suf_array, lcp_array = build_from_tokens(tokens)
        self.assertEqual(1, len(suf_array))
        self.assertEqual(0, suf_array[0])

    def test_two_equal_words(self):
        tokens = self.tokenizer.tokenize("one two three four two five", self.config)
        suf_array, lcp_array = build_from_tokens(tokens)
        self.assertEqual(1, suf_array[1])
        self.assertEqual(4, suf_array[2])

    def test_lcp_format(self):
        tokens = self.tokenizer.tokenize("one two three four two five", self.config)
        suf_array, lcp_array = build_from_tokens(tokens)
        self.assertEqual(-1, lcp_array[0])

    def test_lcp(self):
        tokens = self.tokenizer.tokenize("one two three four two five", self.config)
        suf_array, lcp_array = build_from_tokens(tokens)
        self.assertEqual(1, lcp_array[2])


if __name__ == '__main__':
    unittest.main()
