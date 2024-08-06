import pytest
from model.lexical_entry import LexicalEntry
from model.common_enums import CharacterType
from db.mysql_repository import MySQLRepository

@pytest.fixture
def repo():
    # Initialize the repository with the test database settings
    return MySQLRepository(
        host='localhost',
        user='root',
        password='root',
        database='devanagari'
    )

def test_add_and_get_character(repo):
    # Define a character to insert into the database
    character = LexicalEntry(
        symbol='अ',
        name='A',
        type=CharacterType.VOWEL,
        pronunciation='a',
        translation=Translation('', '')  # Adjust if needed
    )

    # Add the character to the database
    repo.add_character(character)

    # Retrieve the character from the database
    result = repo.get_character('अ')

    # Verify that the retrieved character matches the inserted character
    assert result == character

def test_get_nonexistent_character(repo):
    # Try to retrieve a character that doesn't exist
    result = repo.get_character('999')  # Assuming this symbol does not exist

    # Verify that the result is None
    assert result is None
