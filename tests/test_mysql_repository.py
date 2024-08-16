import pytest
from db.mysql_repository import MysqlRepository
from model.lexical_entry import LexicalEntry, CharacterType
from model.word import Word

@pytest.fixture
def repo():
    return MysqlRepository(host="localhost", user="root", password="rootpassword", database="devanagari")

def test_get_character(repo):
    char = repo.get_character('अ')
    assert char is not None
    assert char.symbol == 'अ'
    assert char.name == 'a'
    assert char.type == CharacterType.VOWEL
    assert char.pronunciation == "/a/ ('a' in 'about')"

def test_get_all_characters(repo):
    chars = repo.get_all_characters()
    assert len(chars) > 0
    assert all(isinstance(char, LexicalEntry) for char in chars)

def test_add_character(repo):
    new_char = LexicalEntry('ौ', 'au', CharacterType.VOWEL, "/au/ ('ou' in 'out')")
    repo.add_character(new_char)
    added_char = repo.get_character('ौ')
    assert added_char is not None
    assert added_char.name == 'au'

def test_get_word(repo):
    word = repo.get_word('नमस्ते')
    assert word is not None
    assert word.word_form == 'नमस्ते'
    assert word.transliteration == 'namaste'

def test_add_word(repo):
    new_word = Word('शुभ', 'shubh', 'shubh')
    repo.add_word(new_word)
    added_word = repo.get_word('शुभ')
    assert added_word is not None
    assert added_word.transliteration == 'shubh'