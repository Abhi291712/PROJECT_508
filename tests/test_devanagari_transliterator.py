import unittest
from model.devanagari_analyzer import WordTransliterator

class TestWordTransliterator(unittest.TestCase):

    def setUp(self):
        self.transliterator = WordTransliterator()

    def test_transliterate_valid_word(self):
        # Test that a valid Devanagari word is correctly transliterated
        word = "अआइ"
        expected_transliteration = "aāi"
        result = self.transliterator.transliterate(word)
        self.assertEqual(result, expected_transliteration)

    def test_transliterate_invalid_word(self):
        # Test that a word containing unknown characters returns None
        word = "अॠइ"  # Assuming "ॠ" is not in the transliteration map
        result = self.transliterator.transliterate(word)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

