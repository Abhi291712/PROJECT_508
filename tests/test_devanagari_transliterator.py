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
        self.assertEqual(result, "aāX")  # Unknown character is kept as-is

    def test_transliterate_partial_valid_word(self):
        result = self.transliterator.transliterate("अआइX")
        self.assertEqual(result, "aāiX")  # Unknown character is kept as-is

    def test_transliterate_word_with_invalid_characters(self):
        result = self.transliterator.transliterate("अआX123")
        self.assertEqual(result, "aāX123")  # Invalid characters are kept as-is

    def test_transliterate_empty_string(self):
        result = self.transliterator.transliterate("")
        self.assertEqual(result, "")  # Empty string returns empty string

    def test_transliterate_with_virama(self):
        result = self.transliterator.transliterate("क्")
        self.assertEqual(result, "k")  # Virama removes inherent 'a'

    def test_transliterate_complex_word(self):
        result = self.transliterator.transliterate("नमस्ते")
        self.assertEqual(result, "namaste")

if __name__ == '__main__':
    unittest.main()