import unittest
from model.word_transliterator import WordTransliterator


class TestWordTransliterator(unittest.TestCase):

    def setUp(self):
        self.transliterator = WordTransliterator()

    def test_transliterate_word(self):
        result = self.transliterator.transliterate("अआइउ")
        self.assertEqual(result, "aāiu")

    def test_transliterate_unknown_character(self):
        result = self.transliterator.transliterate("अआX")
        self.assertIsNone(result)

    def test_transliterate_partial_valid_word(self):
        result = self.transliterator.transliterate("अआइX")
        self.assertIsNone(result)

    def test_transliterate_word_with_invalid_characters(self):
        result = self.transliterator.transliterate("अआX")
        self.assertIsNone(result)

    def test_transliterate_empty_string(self):
        result = self.transliterator.transliterate("")
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
