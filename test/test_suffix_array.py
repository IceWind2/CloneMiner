import unittest
import TextDuplicateSearch.TextProcessing.Tokenizer as Tokenizer
import TextDuplicateSearch.StrictSearch.SuffixArray as SuffixArray


class UnitSuffixArray(unittest.TestCase):
    def setUp(self) -> None:
        Tokenizer.reset()

    def test_empty(self):
        test_array = []
        suf_array = SuffixArray._build_suffix_array(test_array)
        self.assertEqual(0, len(suf_array))

    def test_one_word(self):
        test_array = [0]
        suf_array = SuffixArray._build_suffix_array(test_array)
        self.assertEqual(1, len(suf_array))
        self.assertEqual(0, suf_array[0])

    def test_two_equal_words(self):
        test_array = [1, 2, 3, 4, 2, 5]
        suf_array = SuffixArray._build_suffix_array(test_array)
        self.assertEqual(1, suf_array[1])
        self.assertEqual(4, suf_array[2])

    def test_lcp_format(self):
        test_array = [1, 2, 3, 4, 2, 5]
        suf_array = SuffixArray._build_suffix_array(test_array)
        lcp_array = SuffixArray._build_lcp_array(test_array, suf_array)
        self.assertEqual(-1, lcp_array[0])

    def test_lcp(self):
        test_array = [1, 2, 3, 4, 2, 5]
        suf_array = SuffixArray._build_suffix_array(test_array)
        lcp_array = SuffixArray._build_lcp_array(test_array, suf_array)
        self.assertEqual(1, lcp_array[2])


class IntegrationSuffixArray(unittest.TestCase):
    def setUp(self) -> None:
        Tokenizer.reset()

    def test_empty(self):
        tokens = Tokenizer.tokenize("", "")
        suf_array, lcp_array = SuffixArray.build_from_tokens(tokens)
        self.assertEqual(0, len(suf_array))

    def test_one_word(self):
        tokens = Tokenizer.tokenize("one", "")
        suf_array, lcp_array = SuffixArray.build_from_tokens(tokens)
        self.assertEqual(1, len(suf_array))
        self.assertEqual(0, suf_array[0])

    def test_two_equal_words(self):
        tokens = Tokenizer.tokenize("one two three four two five", "")
        suf_array, lcp_array = SuffixArray.build_from_tokens(tokens)
        self.assertEqual(1, suf_array[1])
        self.assertEqual(4, suf_array[2])

    def test_lcp_format(self):
        tokens = Tokenizer.tokenize("one two three four two five", "")
        suf_array, lcp_array = SuffixArray.build_from_tokens(tokens)
        self.assertEqual(-1, lcp_array[0])

    def test_lcp(self):
        tokens = Tokenizer.tokenize("one two three four two five", "")
        suf_array, lcp_array = SuffixArray.build_from_tokens(tokens)
        self.assertEqual(1, lcp_array[2])


if __name__ == '__main__':
    unittest.main()
