
import unittest
from model.devanagari_analyzer import CharacterIdentifier, LexicalEntry, CharacterType

class TestCharacterIdentifier(unittest.TestCase):

    def setUp(self):
        self.identifier = CharacterIdentifier()

    def test_identify_valid_character(self):
        # Test that a valid character returns the correct LexicalEntry
        char = "अ"
        expected_entry = LexicalEntry("अ", "a", CharacterType.VOWEL, "/ə/", 
                                      Translation("a", "The first letter of the Devanagari script"))
        result = self.identifier.identify(char)
        self.assertEqual(result, expected_entry)

    def test_identify_invalid_character(self):
        # Test that an invalid character returns None
        char = "ॠ"  # Assuming this character is not in char_info
        result = self.identifier.identify(char)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
