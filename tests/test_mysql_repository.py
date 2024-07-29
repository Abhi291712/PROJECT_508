import pytest
from db.mysql_repository import MySQLRepository


@pytest.fixture
def repo():
    return MySQLRepository(
        host='localhost',
        user='root',
        password='root',
        database='devanagari'
    )


def test_add_and_get_character(repo):
    # Add a character
    repo.add_character('न', 'Na', 'CONSONANT', 'na')

    # Retrieve the character
    character = repo.get_character('न')

    # Check if the character is as expected
    assert character is not None
    assert character[1] == 'Na'
    assert character[2] == 'CONSONANT'
    assert character[3] == 'na'


def test_get_nonexistent_character(repo):
    # Try retrieving a character that does not exist
    character = repo.get_character('अ')

    # Ensure that it does not return None or incorrect data
    assert character is not None
    assert character[1] == 'A'
    assert character[2] == 'VOWEL'
    assert character[3] == 'a'
