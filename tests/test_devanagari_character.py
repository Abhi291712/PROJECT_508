import unittest
from model.character_identifier import CharacterIdentifier

class TestCharacterIdentifier(unittest.TestCase):

    def setUp(self):
        self.identifier = CharacterIdentifier()

    def test_identify_vowel(self):
        result = self.identifier.identify_character("अ")
        self.assertEqual(result, {"name": "a", "type": "Vowel", "pronunciation": "/a/ ('a' in 'about')"})

    def test_identify_consonant(self):
        result = self.identifier.identify_character("क")
        self.assertEqual(result, {"name": "ka", "type": "Consonant", "pronunciation": "/kə/ ('k' in 'kite')"})

    def test_identify_unknown_character(self):
        result = self.identifier.identify_character("X")
        self.assertEqual(result, {"error": "Character not found"})

    def test_identify_empty_string(self):
        result = self.identifier.identify_character("")
        self.assertEqual(result, {"error": "Character not found"})

    def test_identify_multiple_characters(self):
        result = self.identifier.identify_character("अक")
        self.assertEqual(result, {"error": "Character not found"})

    def test_identify_special_character(self):
        result = self.identifier.identify_character("ं")
        self.assertEqual(result, {"error": "Character not found"})  # Assuming anusvara is not in the character set

    def test_identify_all_vowels(self):
        vowels = "अआइईउऊएऐओऔ"
        for vowel in vowels:
            result = self.identifier.identify_character(vowel)
            self.assertEqual(result["type"], "Vowel")

    def test_identify_all_consonants(self):
        consonants = "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह"
        for consonant in consonants:
            result = self.identifier.identify_character(consonant)
            self.assertEqual(result["type"], "Consonant")

if __name__ == '__main__':
    unittest.main()