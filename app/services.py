# app/services.py
from db.repository import Repository
from model.character_identifier import CharacterIdentifier
from model.word_transliterator import WordTransliterator

class Services:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.character_identifier = CharacterIdentifier()
        self.word_transliterator = WordTransliterator()

    def get_character_info(self, symbol: str):
        character = self.repo.get_character(symbol)
        if character:
            return self.character_identifier.identify_character(character.symbol)
        return {"error": "Character not found"}

    def transliterate_word(self, word: str):
        if not all(char in self.word_transliterator.transliteration_map for char in word):
            return "Error: Input contains non-Devanagari characters"
        return self.word_transliterator.transliterate(word)