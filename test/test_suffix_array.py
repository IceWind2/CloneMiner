import unittest
import TextDuplicateSearch.Tokenizer as Tokenizer
import TextDuplicateSearch.SuffixArray as SuffixArray


class TestSuffixArray(unittest.TestCase):
    def setUp(self) -> None:
        Tokenizer.reset()

    def test_empty(self):
        tokens = Tokenizer.tokenize("", "")
        suf_array, lcp_array = SuffixArray.build_suffix_array(tokens)
        self.assertEqual(0, len(suf_array))

    def test_one_word(self):
        tokens = Tokenizer.tokenize("one", "")
        suf_array, lcp_array = SuffixArray.build_suffix_array(tokens)
        self.assertEqual(1, len(suf_array))
        self.assertEqual(0, suf_array[0])

    def test_two_equal_words(self):
        tokens = Tokenizer.tokenize("one two three four two five", "")
        suf_array, lcp_array = SuffixArray.build_suffix_array(tokens)
        self.assertEqual(1, suf_array[1])
        self.assertEqual(4, suf_array[2])

    def test_lcp(self):
        tokens = Tokenizer.tokenize("one two three four two five", "")
        suf_array, lcp_array = SuffixArray.build_suffix_array(tokens)
        self.assertEqual(1, lcp_array[2])


if __name__ == '__main__':
    unittest.main()
