import unittest
from unittest.mock import MagicMock
from app.services import DevanagariService
from model import LexicalEntry, CharacterType

class TestDevanagariService(unittest.TestCase):
    def setUp(self):
        self.mock_repository = MagicMock()
        self.service = DevanagariService(self.mock_repository)

    def test_identify_character_found(self):
        # Mock the repository response
        character = LexicalEntry(
            symbol="अ",
            name="a",
            type=CharacterType.VOWEL,
            pronunciation="/a/ ('a' in 'about')",
            translation="a"
        )
        self.mock_repository.get_character_by_symbol.return_value = character
        
        # Test the service method
        result = self.service.identify_character("अ")
        expected_result = {
            "symbol": "अ",
            "name": "a",
            "type": "Vowel",
            "pronunciation": "/a/ ('a' in 'about')",
            "translation": "a"
        }
        
        self.assertEqual(result, expected_result)

    def test_identify_character_not_found(self):
        # Mock the repository response
        self.mock_repository.get_character_by_symbol.return_value = None
        
        # Test the service method
        result = self.service.identify_character("unknown")
        self.assertEqual(result, "Character not found")

if __name__ == "__main__":
    unittest.main()
