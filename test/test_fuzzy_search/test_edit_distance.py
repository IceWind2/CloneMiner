import unittest

from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.DataModels.TextFragment import TextFragment
from TextDuplicateSearch.DuplicateSearch.FuzzySearch.Tools.EditDistance import DamerauLevenshtein, UkkonenAsm


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=False,
                                   min_dup_length=3)

        self.edit_distance = DamerauLevenshtein(2)

    def test_both_empty(self):
        frg1 = TextFragment([])
        frg2 = TextFragment([])
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(0, dist)

    def test_one_empty(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(4, dist)

    def test_insert(self):
        self.edit_distance.define_costs(insert=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three ", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_delete(self):
        self.edit_distance.define_costs(delete=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_substitute(self):
        self.edit_distance.define_costs(substitute=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two four", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_transpose(self):
        self.edit_distance.define_costs(transpose=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three two", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_multiple_1(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three four two one", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(4, dist)

    def test_multiple_2(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one three four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(6, dist)


class TestUkkonenAsm(unittest.TestCase):
    def setUp(self) -> None:
        self.tokenizer = Tokenizer()
        self.config = SearchConfig(input_file="",
                                   output_file="",
                                   need_text_processing=False,
                                   min_dup_length=3)
        
        self.edit_distance = UkkonenAsm(2)

    def test_both_empty(self):
        frg1 = TextFragment([])
        frg2 = TextFragment([])
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(0, dist)

    def test_one_empty(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(4, dist)

    def test_insert(self):
        self.edit_distance.define_costs(insert=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three ", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_delete(self):
        self.edit_distance.define_costs(delete=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_substitute(self):
        self.edit_distance.define_costs(substitute=1)
        frg1 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two four", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(1, dist)

    def test_multiple_1(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one two four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one three four two one", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(6, dist)

    def test_multiple_2(self):
        frg1 = TextFragment(self.tokenizer.tokenize("one three four one two", self.config))
        frg2 = TextFragment(self.tokenizer.tokenize("one two three", self.config))
        dist = self.edit_distance.calculate(frg1, frg2)
        self.assertEqual(8, dist)


if __name__ == '__main__':
    unittest.main()
