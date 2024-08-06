import pytest
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
    character = {
        'id': 1,
        'symbol': 'अ',
        'name': 'A',
        'type': 'Vowel',
        'pronunciation': 'a'
    }

    # Add the character to the database
    repo.add_character(character)

    # Retrieve the character from the database
    result = repo.get_character(1)

    # Verify that the retrieved character matches the inserted character
    assert result == {
        'id': 1,
        'symbol': 'अ',
        'name': 'A',
        'type': 'Vowel',
        'pronunciation': 'a'
    }


def test_get_nonexistent_character(repo):
    # Try to retrieve a character that doesn't exist
    result = repo.get_character(999)  # Assuming this ID does not exist

    # Verify that the result is None
    assert result is None

