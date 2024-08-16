import pytest
from app.services import Services
from db.repository import Repository
from model.lexical_entry import LexicalEntry, CharacterType
from model.word import Word

class MockRepository(Repository):
    def __init__(self):
        self.characters = {}
        self.words = {}

    def get_character(self, symbol: str):
        return self.characters.get(symbol)

    def get_all_characters(self):
        return list(self.characters.values())

    def add_character(self, entry: LexicalEntry):
        self.characters[entry.symbol] = entry

    def get_word(self, word_form: str):
        return self.words.get(word_form)

    def add_word(self, word: Word):
        self.words[word.word_form] = word

@pytest.fixture
def services():
    repo = MockRepository()
    repo.add_character(LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/ ('a' in 'about')"))
    repo.add_character(LexicalEntry("क", "ka", CharacterType.CONSONANT, "/kə/ ('k' in 'kite')"))
    repo.add_word(Word("नमस्ते", transliteration="namaste"))
    return Services(repo)

def test_get_character_info(services):
    info = services.get_character_info("अ")
    assert info == {
        "symbol": "अ",
        "name": "a",
        "type": "VOWEL",
        "pronunciation": "/a/ ('a' in 'about')"
    }

def test_get_character_info_not_found(services):
    info = services.get_character_info("ौ")
    assert info == {"error": "Character not found"}

def test_transliterate_word(services):
    result = services.transliterate_word("नमस्ते")
    assert result == "namaste"

def test_transliterate_word_not_in_db(services):
    result = services.transliterate_word("शुभ")
    assert result == "śubha"

def test_transliterate_word_invalid_input(services):
    result = services.transliterate_word("hello")
    assert result == "Error: Input contains non-Devanagari characters"

def test_transliterate_word_empty_input(services):
    result = services.transliterate_word("")
    assert result == "Error: Input is empty"

def test_get_all_characters(services):
    characters = services.get_all_characters()
    assert len(characters) == 2
    assert characters[0]["symbol"] == "अ"
    assert characters[1]["symbol"] == "क"