import unittest

from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.Tools.Hashing import Hashing


class TestSignatureHashing(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=False,
                                   min_dup_length=3)

    def test_empty(self):
        hash_sign = Hashing.signature_hash_func([])
        self.assertEqual(0, hash_sign)

    def test_one_letter(self):
        tokens = self.tokenizer.tokenize("abc", self.config)
        hash_sign = Hashing.signature_hash_func(tokens)
        self.assertEqual(256, hash_sign)

    def test_one_symbol(self):
        tokens = self.tokenizer.tokenize("№$#", self.config)
        hash_sign = Hashing.signature_hash_func(tokens)
        self.assertEqual(1, hash_sign)

    def test_multiple_bits_1(self):
        tokens = self.tokenizer.tokenize("abc dfg", self.config)
        hash_sign = Hashing.signature_hash_func(tokens)
        self.assertEqual(256 + 128, hash_sign)

    def test_multiple_bits_2(self):
        tokens = self.tokenizer.tokenize("b g, j, x", self.config)
        hash_sign = Hashing.signature_hash_func(tokens)
        self.assertEqual(256 + 64 + 32 + 2, hash_sign)


if __name__ == '__main__':
    unittest.main()
