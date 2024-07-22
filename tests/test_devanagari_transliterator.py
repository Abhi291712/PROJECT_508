import unittest
from model.word_transliterator import WordTransliterator

class TestWordTransliterator(unittest.TestCase):
    
    def setUp(self):
        self.transliterator = WordTransliterator()
    
    def test_transliterate_valid_word(self):
        result = self.transliterator.transliterate("अआइ")
        self.assertEqual(result, "aāi")
    
    def test_transliterate_partial_valid_word(self):
        result = self.transliterator.transliterate("अआइअ")
        self.assertIsNone(result)
    
    def test_transliterate_empty_word(self):
        result = self.transliterator.transliterate("")
        self.assertEqual(result, "")
    
    def test_transliterate_invalid_character(self):
        result = self.transliterator.transliterate("अx")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
