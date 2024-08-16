import pytest
from app import app
from app.services import Services
from db.repository import Repository
from model.lexical_entry import LexicalEntry, CharacterType

class MockRepository(Repository):
    def get_character(self, symbol: str):
        if symbol == "अ":
            return LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/ ('a' in 'about')")
        return None

    def get_all_characters(self):
        return [LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/ ('a' in 'about')")]

    def add_character(self, entry):
        pass

    def get_word(self, word_form: str):
        if word_form == "नमस्ते":
            return LexicalEntry("नमस्ते", "namaste", None, None)
        return None

    def add_word(self, word):
        pass

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.services = Services(MockRepository())
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Devanagari Translator API" in response.data

def test_identify_character(client):
    response = client.post('/identify', json={'character': 'अ'})
    assert response.status_code == 200
    data = response.get_json()
    assert data['symbol'] == 'अ'
    assert data['name'] == 'a'
    assert data['type'] == 'VOWEL'
    assert data['pronunciation'] == "/a/ ('a' in 'about')"

def test_identify_character_not_found(client):
    response = client.post('/identify', json={'character': 'ौ'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == "Character not found"

def test_identify_character_no_input(client):
    response = client.post('/identify', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == "No character provided"

def test_transliterate_word(client):
    response = client.post('/transliterate', json={'word': 'नमस्ते'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'transliterated_word' in data
    assert data['transliterated_word'] == "namaste"

def test_transliterate_word_not_in_db(client):
    response = client.post('/transliterate', json={'word': 'शुभ'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'transliterated_word' in data
    assert data['transliterated_word'] == "śubha"

def test_transliterate_word_no_input(client):
    response = client.post('/transliterate', json={})
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
    assert data['error'] == "No word provided"

def test_get_all_characters(client):
    response = client.get('/characters')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]['symbol'] == 'अ'
    assert data[0]['name'] == 'a'
    assert data[0]['type'] == 'VOWEL'
    assert data[0]['pronunciation'] == "/a/ ('a' in 'about')"

def test_serve_ui(client):
    response = client.get('/ui')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data
    assert b'Devanagari Translator' in response.data