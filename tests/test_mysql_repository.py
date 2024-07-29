import pytest
from mysql_repository import MySQLRepository
from model.lexical_entry import LexicalEntry, Translation
from model.common_enums import CharacterType

@pytest.fixture
def repo():
    return MySQLRepository(host='localhost', user='root', password='your_password',
                           database='devanagari')

def test_get_character(repo):
    # Add a character to the database for testing
    repo.add_character(LexicalEntry(
        symbol='अ',
        name='A',
        type=CharacterType.Vowel,
        pronunciation='',  # Adjust as necessary
        translation=Translation('', '')  # Adjust as necessary
    ))

    char = repo.get_character('अ')
    assert char is not None
    assert char.symbol == 'अ'
    assert char.name == 'A'
    assert char.type == CharacterType.Vowel

def test_add_and_get_character(repo):
    new_char = LexicalEntry(
        symbol='ब',
        name='Ba',
        type=CharacterType.Consonant,
        pronunciation='',  # Adjust as necessary
        translation=Translation('ba', 'Second consonant of Devanagari script')
    )
    repo.add_character(new_char)

    retrieved_char = repo.get_character('ब')
    assert retrieved_char is not None
    assert retrieved_char.symbol == 'ब'
    assert retrieved_char.name == 'Ba'
    assert retrieved_char.type == CharacterType.Consonant

def test_get_word_transliteration(repo):
    # Add a word to the database for testing
    repo.add_word_transliteration('नमस्ते', 'namaste')

    transliteration = repo.get_word_transliteration('नमस्ते')
    assert transliteration == 'namaste'

def test_add_and_get_word_transliteration(repo):
    repo.add_word_transliteration('शुभ प्रभात', 'shubh prabhaat')
    transliteration = repo.get_word_transliteration('शुभ प्रभात')
    assert transliteration == 'shubh prabhaat'
