# app/services.py
from typing import Dict, Optional
from db.mysql_repository import MySQLRepository
from model.character_identifier import CharacterIdentifier
from model.word_transliterator import WordTransliterator

class Services:
    def __init__(self):
        self.repo = MySQLRepository()
        self.character_identifier = CharacterIdentifier()
        self.word_transliterator = WordTransliterator()

    # Use case 1: the app takes a single Devanagari character and returns information about it
    def get_character_info(self, symbol: str) -> Dict[str, str]:
        # Fetch character details from the character_identifier
        character_info = self.character_identifier.identify_character(symbol)

        if "error" not in character_info:
            return {
                "iconic_symbol": symbol,
                "name": character_info["name"],
                "type": character_info["type"],
                "pronunciation": character_info["pronunciation"]
            }
        else:
            return character_info

    # Use case 2: the app takes a Devanagari word and returns its Latin script transliteration
    def transliterate_word(self, devanagari_word: str) -> Optional[str]:
        # Check if all characters are valid Devanagari characters
        if all(char in self.word_transliterator.transliteration_map for char in devanagari_word):
            return self.word_transliterator.transliterate(devanagari_word)
        else:
            return "Error: Input contains non-Devanagari characters"

# Example usage
if __name__ == "__main__":
    services = Services()

    # Example usage for character identification
    character_info = services.get_character_info('अ')
    print(character_info)  # Output: {'iconic_symbol': 'अ', 'name': 'a', 'type': 'Vowel', 'pronunciation': '/a/ ('a' in 'about')'}

    # Example usage for word transliteration
    transliterated_word = services.transliterate_word('नमस्ते')
    print(transliterated_word)  # Output: 'namaste'
