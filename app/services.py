from db.repository import Repository
from model.lexical_entry import LexicalEntry
from model.word import Word
from model.word_transliterator import WordTransliterator


class Services:
    def __init__(self, repo: Repository):
        self.repo = repo
        self.transliterator = WordTransliterator()

    def get_character_info(self, symbol: str) -> dict:
        character = self.repo.get_character(symbol)
        if character:
            return {
                "symbol": character.symbol,
                "name": character.name,
                "type": character.type.value,
                "pronunciation": character.pronunciation
            }
        return {"error": "Character not found"}

    def transliterate_word(self, word: str) -> str:
        if not word:
            return "Error: Input is empty"

        if not all('\u0900' <= char <= '\u097F' for char in word):
            return "Error: Input contains non-Devanagari characters"

        stored_word = self.repo.get_word(word)
        if stored_word and stored_word.transliteration:
            return stored_word.transliteration

        transliteration = self.transliterator.transliterate(word)
        self.repo.add_word(Word(word, transliteration=transliteration))
        return transliteration

    def get_all_characters(self) -> list:
        characters = self.repo.get_all_characters()
        return [
            {
                "symbol": char.symbol,
                "name": char.name,
                "type": char.type.value,
                "pronunciation": char.pronunciation
            }
            for char in characters
        ]