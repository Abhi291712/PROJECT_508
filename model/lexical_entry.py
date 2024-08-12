from enum import Enum

class CharacterType(Enum):
    VOWEL = "VOWEL"
    CONSONANT = "CONSONANT"
    SPECIAL = "SPECIAL"

class LexicalEntry:
    def __init__(self, symbol: str, name: str, type: CharacterType, pronunciation: str):
        self.symbol = symbol
        self.name = name
        self.type = type
        self.pronunciation = pronunciation

    def __str__(self):
        return f"LexicalEntry(symbol={self.symbol}, name={self.name}, type={self.type}, pronunciation={self.pronunciation})"