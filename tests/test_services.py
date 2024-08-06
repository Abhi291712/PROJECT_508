import unittest
from app.services import Services

class TestServices(unittest.TestCase):

    def setUp(self):
        self.services = Services()

    def test_get_character_info(self):
        result = self.services.get_character_info('अ')
        expected = {
            "iconic_symbol": "अ",
            "name": "a",
            "type": "Vowel",
            "pronunciation": "/a/ ('a' in 'about')"
        }
        self.assertEqual(result, expected)

    def test_transliterate_word(self):
        result = self.services.transliterate_word('नमस्ते')
        expected = 'namaste'
        self.assertEqual(result, expected)

    def test_transliterate_word_invalid(self):
        result = self.services.transliterate_word('hello')
        expected = "Error: Input contains non-Devanagari characters"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
