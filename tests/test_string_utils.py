import unittest

from utils.string_utils import capitalize_words, reverse, word_count


class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(""), "")

    def test_single_char(self):
        self.assertEqual(reverse("a"), "a")

    def test_word(self):
        self.assertEqual(reverse("hello"), "olleh")


class TestCapitalizeWords(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(capitalize_words(""), "")

    def test_single_word(self):
        self.assertEqual(capitalize_words("hello"), "Hello")

    def test_multiple_words(self):
        self.assertEqual(capitalize_words("hello world"), "Hello World")

    def test_repeated_whitespace_collapses(self):
        self.assertEqual(capitalize_words("  hello   world  "), "Hello World")

    def test_lowercases_rest_of_word(self):
        self.assertEqual(capitalize_words("hELLO"), "Hello")


class TestWordCount(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_whitespace_only(self):
        self.assertEqual(word_count("   "), 0)

    def test_single_word(self):
        self.assertEqual(word_count("hello"), 1)

    def test_multiple_words(self):
        self.assertEqual(word_count("hello world foo"), 3)

    def test_repeated_whitespace(self):
        self.assertEqual(word_count("  hello   world  "), 2)


if __name__ == "__main__":
    unittest.main()
