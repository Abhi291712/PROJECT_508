import pytest
from app.services import Services
from db.mysql_repository import MysqlRepository
import os

@pytest.fixture
def services():
    host = os.getenv('DB_HOST', '127.0.0.1')
    user = os.getenv('DB_USER', 'root')
    password = os.getenv('DB_PASSWORD', 'root')
    database = os.getenv('DB_NAME', 'devanagari')

    repo = MysqlRepository(host=host, user=user, password=password, database=database)
    return Services(repo)

def test_get_character_info(services):
    result = services.get_character_info('अ')
    expected = {
        "iconic_symbol": "अ",
        "name": "a",
        "type": "Vowel",
        "pronunciation": "/a/ ('a' in 'about')"
    }
    assert result == expected

def test_transliterate_word(services):
    result = services.transliterate_word('नमस्ते')
    assert result == 'namaste'

def test_transliterate_word_invalid(services):
    result = services.transliterate_word('hello')
    assert result == "Error: Input contains non-Devanagari characters"

def test_get_nonexistent_character_info(services):
    result = services.get_character_info('nonexistent')
    expected = {"error": "Character not found"}
    assert result == expected

def test_transliterate_empty_word(services):
    result = services.transliterate_word('')
    assert result == "Error: Input is empty"
