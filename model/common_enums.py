from enum import Enum

class CharacterType(Enum):
    VOWEL = "Vowel"
    CONSONANT = "Consonant"
    SPECIAL = "Special"

class ErrorCode(Enum):
    CHARACTER_NOT_FOUND = "Character not found"
    INVALID_INPUT = "Invalid input"
