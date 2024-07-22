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
        transliterated_chars = []
        for char in word:
            if char in self.transliteration_map:
                transliterated_chars.append(self.transliteration_map[char])
            else:
                return None  # Return None if any character is not in the transliteration map
        return ''.join(transliterated_chars)
