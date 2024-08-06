import mysql.connector
from typing import Optional
from model import LexicalEntry, CharacterType  # Change from relative to absolute import

class MySQLRepository:
    def __init__(self, host: str, user: str, password: str, database: str):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database= devanagari
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()

    def add_character(self, entry: LexicalEntry) -> None:
        query = """
        INSERT INTO devanagari_characters (character, name, type, pronunciation)
        VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(query, (
            entry.symbol,
            entry.name,
            entry.type.name,
            entry.pronunciation
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
                pronunciation=result['pronunciation'],
                translation=''  # Adjust as necessary
            )
        return None
