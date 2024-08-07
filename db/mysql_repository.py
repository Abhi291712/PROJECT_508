import mysql.connector
from typing import Optional
from model.lexical_entry import LexicalEntry, CharacterType
from db.repository import Repository

class MysqlRepository(Repository):
    def __init__(self, host: str, user: str, password: str, database: str):
        super().__init__()
        config = {
            'user': user,
            'password': password,
            'host': host,
            'database': database
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor(dictionary=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def add_character(self, entry: LexicalEntry) -> None:
        query = """
        INSERT INTO devanagari_characters (character, name, type)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (
            entry.symbol,
            entry.name,
            entry.type.name
        ))
        self.connection.commit()

    def get_character(self, symbol: str) -> Optional[LexicalEntry]:
        query = "SELECT * FROM devanagari_characters WHERE character = %s"
        self.cursor.execute(query, (symbol,))
        result = self.cursor.fetchone()
        if result:
            return LexicalEntry(
                symbol=result['character'],
                name=result['name'],
                type=CharacterType[result['type']],
                pronunciation=''  # Adjust as necessary
            )
        return None

    def add_word_transliteration(self, word: str, transliteration: str) -> None:
        query = """
        INSERT INTO words (devanagari_word, latin_transliteration)
        VALUES (%s, %s)
        """
        self.cursor.execute(query, (word, transliteration))
        self.connection.commit()

    def get_word_transliteration(self, word: str) -> Optional[str]:
        query = "SELECT latin_transliteration FROM words WHERE devanagari_word = %s"
        self.cursor.execute(query, (word,))
        result = self.cursor.fetchone()
        if result:
            return result['latin_transliteration']
        return None

    def get_all_characters(self) -> list:
        query = "SELECT * FROM devanagari_characters"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [LexicalEntry(
            symbol=row['character'],
            name=row['name'],
            type=CharacterType[row['type']],
            pronunciation=''
        ) for row in results]
