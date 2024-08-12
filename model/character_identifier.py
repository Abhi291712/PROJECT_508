# model/character_identifier.py

class CharacterIdentifier:
    def __init__(self):
        self.characters = {
            "अ": {"name": "a", "type": "Vowel", "pronunciation": "/a/ ('a' in 'about')"},
            "आ": {"name": "ā", "type": "Vowel", "pronunciation": "/ɑː/ ('a' in 'father')"},
            "इ": {"name": "i", "type": "Vowel", "pronunciation": "/i/ ('i' in 'sit')"},
            "ई": {"name": "ī", "type": "Vowel", "pronunciation": "/iː/ ('ee' in 'see')"},
            "उ": {"name": "u", "type": "Vowel", "pronunciation": "/u/ ('u' in 'put')"},
            "ऊ": {"name": "ū", "type": "Vowel", "pronunciation": "/uː/ ('oo' in 'boot')"},
            "ए": {"name": "e", "type": "Vowel", "pronunciation": "/e/ ('e' in 'bed')"},
            "ऐ": {"name": "ai", "type": "Vowel", "pronunciation": "/ai/ ('ai' in 'aisle')"},
            "ओ": {"name": "o", "type": "Vowel", "pronunciation": "/o/ ('o' in 'go')"},
            "औ": {"name": "au", "type": "Vowel", "pronunciation": "/au/ ('ou' in 'out')"},
            "क": {"name": "ka", "type": "Consonant", "pronunciation": "/kə/ ('k' in 'kite')"},
            "ख": {"name": "kha", "type": "Consonant", "pronunciation": "/kʰə/ (aspirated 'k' in 'khaki')"},
            "ग": {"name": "ga", "type": "Consonant", "pronunciation": "/gə/ ('g' in 'go')"},
            "घ": {"name": "gha", "type": "Consonant", "pronunciation": "/gʰə/ (aspirated 'g' in 'ghost')"},
            "ङ": {"name": "ṅa", "type": "Consonant", "pronunciation": "/ŋə/ ('ng' in 'sing')"},
            "च": {"name": "ca", "type": "Consonant", "pronunciation": "/tʃə/ ('ch' in 'church')"},
            "छ": {"name": "cha", "type": "Consonant", "pronunciation": "/tʃʰə/ (aspirated 'ch' in 'chair')"},
            "ज": {"name": "ja", "type": "Consonant", "pronunciation": "/dʒə/ ('j' in 'judge')"},
            "झ": {"name": "jha", "type": "Consonant", "pronunciation": "/dʒʰə/ (aspirated 'j' in 'jhā')"},
            "ञ": {"name": "ña", "type": "Consonant", "pronunciation": "/ɲə/ ('ny' in 'canyon')"},
            # Add more consonants and vowels as needed
            "ट": {"name": "ṭa", "type": "Consonant", "pronunciation": "/ʈə/ (retroflex 't' in 'ṭaka')"},
            "ठ": {"name": "ṭha", "type": "Consonant", "pronunciation": "/ʈʰə/ (aspirated retroflex 'ṭha')"},
            "ड": {"name": "ḍa", "type": "Consonant", "pronunciation": "/ɖə/ (retroflex 'd' in 'ḍaka')"},
            "ढ": {"name": "ḍha", "type": "Consonant", "pronunciation": "/ɖʰə/ (aspirated retroflex 'ḍha')"},
            "ण": {"name": "ṇa", "type": "Consonant", "pronunciation": "/ɳə/ ('ṇ' in 'ḍaṇḍa')"},
            # Add more characters...
        }

    def identify_character(self, symbol: str):
        return self.characters.get(symbol, {"error": "Character not found"})
