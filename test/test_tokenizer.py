import unittest
import TextDuplicateSearch.TextProcessing.Tokenizer as Tokenizer


class TestTokenizer(unittest.TestCase):
    def setUp(self) -> None:
        Tokenizer.reset()

    def test_empty(self):
        tokens = Tokenizer.tokenize("", "")
        self.assertEqual(0, len(tokens))

    def test_one_word(self):
        tokens = Tokenizer.tokenize("one", "")
        self.assertEqual("one", tokens[0].txt)

    def test_multiple_words(self):
        tokens = Tokenizer.tokenize("one two three\nfour", "")
        self.assertEqual(4, len(tokens))

    def test_multiple_lines(self):
        tokens = Tokenizer.tokenize("one\n two three\nfour", "")
        self.assertEqual(3, tokens[3].line)

    def test_filter(self):
        tokens = Tokenizer.tokenize("one        two  three,\t four", "")
        self.assertEqual(12, tokens[1].col)
        self.assertEqual("three", tokens[2].txt)
        self.assertEqual("four", tokens[3].txt)


if __name__ == '__main__':
    unittest.main()
