import os
import pytest
from db.mysql_repository import MySQLRepository
from model import LexicalEntry, CharacterType

@pytest.fixture
def repo():
    host = os.getenv('DB_HOST', '127.0.0.1')
    user = os.getenv('DB_USER', 'root')
    password = os.getenv('DB_PASSWORD', 'root')
    database = os.getenv('DB_NAME', 'devanagari')  # Changed to 'devanagari'
    
    with MySQLRepository(host=host, user=user, password=password, database=database) as repo:
        yield repo

def test_add_and_get_character(repo):
    # Define a character to insert into the database
    character = LexicalEntry(
        symbol='अ',
        name='A',
        type=CharacterType.VOWEL,
        pronunciation='a',
        translation=''  # Adjust as needed
    )

    # Add the character to the database
    repo.add_character(character)

    # Retrieve the character from the database
    result = repo.get_character('अ')

    # Verify that the retrieved character matches the inserted character
    assert result.symbol == character.symbol
    assert result.name == character.name
    assert result.type == character.type
    assert result.pronunciation == character.pronunciation

def test_get_nonexistent_character(repo):
    # Try to retrieve a character that doesn't exist
    result = repo.get_character('nonexistent')
    assert result is None
