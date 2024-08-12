class WordTransliterator:
    def __init__(self):
        self.transliteration_map = {
            'अ': 'a', 'आ': 'ā', 'इ': 'i', 'ई': 'ī', 'उ': 'u', 'ऊ': 'ū',
            'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au',
            'क': 'ka', 'ख': 'kha', 'ग': 'ga', 'घ': 'gha', 'ङ': 'ṅa',
            'च': 'ca', 'छ': 'cha', 'ज': 'ja', 'झ': 'jha', 'ञ': 'ña',
            'ट': 'ṭa', 'ठ': 'ṭha', 'ड': 'ḍa', 'ढ': 'ḍha', 'ण': 'ṇa',
            'त': 'ta', 'थ': 'tha', 'द': 'da', 'ध': 'dha', 'न': 'na',
            'प': 'pa', 'फ': 'pha', 'ब': 'ba', 'भ': 'bha', 'म': 'ma',
            'य': 'ya', 'र': 'ra', 'ल': 'la', 'व': 'va',
            'श': 'śa', 'ष': 'ṣa', 'स': 'sa', 'ह': 'ha',
            'ं': 'ṃ', 'ः': 'ḥ', '्': ''
        }

    def transliterate(self, word: str) -> str:
        transliterated = ''
        skip_next = False
        for i, char in enumerate(word):
            if skip_next:
                skip_next = False
                continue
            if char in self.transliteration_map:
                transliterated += self.transliteration_map[char]
                if i < len(word) - 1 and word[i+1] == '्':
                    skip_next = True
                    transliterated = transliterated[:-1]  # Remove the inherent 'a'
            else:
                transliterated += char
        return transliterated