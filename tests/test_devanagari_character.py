import unittest
from model.character_identifier import CharacterIdentifier
from model.lexical_entry import LexicalEntry, Translation
from model.common_enums import CharacterType

class TestCharacterIdentifier(unittest.TestCase):
    
    def setUp(self):
        self.char_identifier = CharacterIdentifier()
    
    def test_identify_existing_character(self):
        result = self.char_identifier.identify("अ")
        self.assertIsNotNone(result)
        self.assertEqual(result.symbol, "अ")
        self.assertEqual(result.name, "a")
        self.assertEqual(result.type, CharacterType.VOWEL)
        self.assertEqual(result.pronunciation, "/ə/")
        self.assertEqual(result.translation.latin, "a")
        self.assertEqual(result.translation.description, "The first letter of the Devanagari script")
    
    def test_identify_non_existing_character(self):
        result = self.char_identifier.identify("ब")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
