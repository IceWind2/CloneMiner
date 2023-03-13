import unittest

from TextDuplicateSearch import Tokenizer
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.Tools.EditDistance import EditDistance


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=False,
                                   min_dup_length=3)
        EditDistance.define_costs(insert=2, delete=2, substitute=2, transpose=2)

    def test_both_empty(self):
        frg1 = TextFragment([])
        frg2 = TextFragment([])
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(0, dist)

    def test_one_empty(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(4, dist)

    def test_insert(self):
        EditDistance.define_costs(insert=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three ", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(1, dist)

    def test_delete(self):
        EditDistance.define_costs(delete=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(1, dist)

    def test_substitute(self):
        EditDistance.define_costs(substitute=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two four", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(1, dist)

    def test_transpose(self):
        EditDistance.define_costs(transpose=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three two", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(1, dist)

    def test_multiple_1(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three four two one", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(4, dist)

    def test_multiple_2(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one three four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        dist = EditDistance.damerau_levenshtein(frg1, frg2)
        self.assertEqual(6, dist)


class TestUkkonenAsm(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=False,
                                   min_dup_length=3)
        EditDistance.define_costs(insert=2, delete=2, substitute=2, transpose=2)

    def test_both_empty(self):
        frg1 = TextFragment([])
        frg2 = TextFragment([])
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(0, dist)

    def test_one_empty(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("", self.config))
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(4, dist)

    def test_insert(self):
        EditDistance.define_costs(insert=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three ", self.config))
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(1, dist)

    def test_delete(self):
        EditDistance.define_costs(delete=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(1, dist)

    def test_substitute(self):
        EditDistance.define_costs(substitute=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two four", self.config))
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(1, dist)

    def test_multiple_1(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three four two one", self.config))
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(6, dist)

    def test_multiple_2(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one three four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        dist = EditDistance.ukkonen_asm(frg1, frg2)
        self.assertEqual(8, dist)


if __name__ == '__main__':
    unittest.main()
