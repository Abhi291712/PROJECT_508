import pytest
from model.character_identifier import CharacterIdentifier

@pytest.fixture
def character_identifier():
    return CharacterIdentifier()

def test_character_identification(character_identifier):
    result = character_identifier.identify_character('अ')
    expected = {
        "name": "a",
        "type": "Vowel",
        "pronunciation": "/a/ ('a' in 'about')"
    }
    assert result == expected

def test_character_identification_nonexistent(character_identifier):
    result = character_identifier.identify_character('nonexistent')
    expected = {"error": "Character not found"}
    assert result == expected

def test_character_identification_with_invalid_symbol(character_identifier):
    result = character_identifier.identify_character(' ')
    expected = {"error": "Character not found"}
    assert result == expected

def test_character_identification_with_empty_string(character_identifier):
    result = character_identifier.identify_character('')
    expected = {"error": "Character not found"}
    assert result == expected

def test_character_identification_for_partial_entry(character_identifier):
    result = character_identifier.identify_character('आ')
    expected = {
        "name": "ā",
        "type": "Vowel",
        "pronunciation": "/ɑː/ ('a' in 'father')"
    }
    assert result == expected

if __name__ == '__main__':
    pytest.main()
