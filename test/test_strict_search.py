import unittest
import TextDuplicateSearch as Search
import TextDuplicateSearch.TextProcessing.Tokenizer as Tokenizer
import inspect
import os


class TestStrictSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.test_directory = os.path.dirname(inspect.getfile(self.__class__))
        self.test_file_name = os.path.join(self.test_directory, "text.txt")
        self.result_file_name = os.path.join(self.test_directory, "res.txt")
        Tokenizer.reset()

    def file_path(self, filename: str) -> str:
        return os.path.join(self.test_directory, filename)

    def test_empty(self):
        Search.find_clones(self.file_path("empty.txt"), 3, self.result_file_name)
        result_file = open(self.result_file_name, encoding='utf-8')
        self.assertEqual("", result_file.read())
        result_file.close()

    def test_text_low_duplicate_length(self):
        data = Search.find_clones(self.test_file_name, 3, self.result_file_name)
        self.assertEqual(176, len(data.cases))

    def test_text_high_duplicate_length(self):
        data = Search.find_clones(self.test_file_name, 20, self.result_file_name)
        self.assertEqual(2, len(data.cases))

    def test_result_file_lines_1(self):
        Search.find_clones(self.test_file_name, 3, self.result_file_name)
        result_file = open(self.result_file_name, encoding='utf-8')
        test = result_file.read()
        self.assertEqual(763, len(test.split('\n')))
        result_file.close()

    def test_result_file_lines_2(self):
        Search.find_clones(self.test_file_name, 20, self.result_file_name)
        result_file = open(self.result_file_name, encoding='utf-8')
        test = result_file.read()
        self.assertEqual(9, len(test.split('\n')))
        result_file.close()


if __name__ == '__main__':
    unittest.main()
