from .common_enums import CharacterType

class Translation:
    def __init__(self, latin: str, description: str):
        self.latin = latin
        self.description = description

class LexicalEntry:
    def __init__(self, symbol: str, name: str, type: CharacterType, pronunciation: str, translation: Translation):
        self.symbol = symbol
        self.name = name
        self.type = type
        self.pronunciation = pronunciation
        self.translation = translation
