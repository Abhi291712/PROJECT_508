from typing import Dict, Optional


class WordTransliterator:
    def __init__(self):
        self.transliteration_map: Dict[str, str] = {
            # Vowels
            "अ": "a",
            "आ": "ā",
            "इ": "i",
            "ई": "ī",
            "उ": "u",
            "ऊ": "ū",
            "ऋ": "ṛ",
            "ॠ": "ṝ",
            "ऌ": "ḷ",
            "ॡ": "ḹ",
            "ए": "e",
            "ऐ": "ai",
            "ओ": "o",
            "औ": "au",

            # Consonants
            "क": "ka",
            "ख": "kha",
            "ग": "ga",
            "घ": "gha",
            "च": "cha",
            "छ": "chha",
            "ज": "ja",
            "झ": "jha",
            "ट": "ṭa",
            "ठ": "ṭha",
            "ड": "ḍa",
            "ढ": "ḍha",
            "ण": "ṇa",
            "त": "ta",
            "थ": "tha",
            "द": "da",
            "ध": "dha",
            "न": "na",
            "प": "pa",
            "फ": "pha",
            "ब": "ba",
            "भ": "bha",
            "म": "ma",
            "य": "ya",
            "र": "ra",
            "ल": "la",
            "व": "va",
            "श": "sha",
            "ष": "ṣa",
            "स": "sa",
            "ह": "ha",
            "ळ": "ḷa",
            "क्ष": "kṣa",
            "ज्ञ": "jñā",

            # Special Characters
            "ं": "ṃ",  # Anusvara
            "ः": "ḥ",  # Visarga
            "।": ".",  # Danda (punctuation)
            "॥": "||",  # Double Danda (punctuation)

            # Additional characters
            "अँ": "aṅ",
            "अः": "aḥ",
            "ॐ": "om",
        }

    def transliterate(self, word: str) -> Optional[str]:
        if not word:  # Check if the input word is empty
            return None
        if not all(char in self.transliteration_map for char in word):
            return None
        return ''.join(self.transliteration_map.get(char, char) for char in word)
