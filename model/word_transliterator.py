from typing import Dict, Optional

class WordTransliterator:
    def __init__(self):
        self.transliteration_map: Dict[str, str] = {
            "अ": "a",
            "आ": "ā",
            "इ": "i",
            # Add more mappings here
        }

    def transliterate(self, word: str) -> Optional[str]:
        if not all(char in self.transliteration_map for char in word):
            return None
        return ''.join(self.transliteration_map.get(char, char) for char in word)
