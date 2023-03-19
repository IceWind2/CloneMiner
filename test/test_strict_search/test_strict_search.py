import unittest
import inspect
import os

from TextDuplicateSearch import StrictDuplicates
from TextDuplicateSearch.DataModels.SearchConfig import SearchConfig
from TextDuplicateSearch.TextProcessing.Tokenizer import Tokenizer


class TestStrictSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.test_directory = os.path.dirname(inspect.getfile(self.__class__))
        self.config = SearchConfig(input_file=os.path.join(self.test_directory, "../text.txt"),
                                   output_file=os.path.join(self.test_directory, "../res.txt"),
                                   min_dup_length=3)

        self.tokenizer = Tokenizer()

    def file_path(self, filename: str) -> str:
        return os.path.join(self.test_directory, filename)

    def test_empty(self):
        self.config.input_file = self.file_path("../empty.txt")
        tokens = self.tokenizer.tokenize_file(self.config)
        data = StrictDuplicates.find_duplicates(tokens, self.config)
        self.assertEqual(0, len(data.cases))

    def test_text_low_duplicate_length(self):
        tokens = self.tokenizer.tokenize_file(self.config)
        data = StrictDuplicates.find_duplicates(tokens, self.config)
        self.assertEqual(176, len(data.cases))

    def test_text_high_duplicate_length(self):
        self.config.min_dup_length = 20
        tokens = self.tokenizer.tokenize_file(self.config)
        data = StrictDuplicates.find_duplicates(tokens, self.config)
        self.assertEqual(2, len(data.cases))

    # def test_result_file_lines_1(self):
    #     Search.find_clones(self.config)
    #     result_file = open(self.config.output_file, encoding='utf-8')
    #     test = result_file.read()
    #     self.assertEqual(763, len(test.split('\n')))
    #     result_file.close()

    # def test_result_file_lines_2(self):
    #     self.config.min_dup_length = 20
    #     Search.find_clones(self.config)
    #     result_file = open(self.config.output_file, encoding='utf-8')
    #     test = result_file.read()
    #     self.assertEqual(9, len(test.split('\n')))
    #     result_file.close()


if __name__ == '__main__':
    unittest.main()
