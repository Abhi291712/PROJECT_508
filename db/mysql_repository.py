import logging
import mysql.connector
from typing import Optional
from model.lexical_entry import LexicalEntry, CharacterType
from db.repository import Repository

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class MysqlRepository(Repository):
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        super().__init__()
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        config = {
            'user': self.user,
            'password': self.password,
            'host': self.host,
            'port': self.port,
            'database': self.database
        }
        logger.debug(f"Attempting to connect to MySQL: host={host}, user={user}, database={database}, port={port}")
        try:
            self.connection = mysql.connector.connect(**config)
            logger.debug("Successfully connected to MySQL")
            self.cursor = self.connection.cursor(dictionary=True)
        except mysql.connector.Error as err:
            logger.error(f"Error connecting to MySQL: {err}")
            raise

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
                pronunciation=''  # Assuming pronunciation is not stored in the database
            )
        return None

    def update_character(self, entry: LexicalEntry) -> None:
        query = """
        UPDATE devanagari_characters
        SET name = %s, type = %s
        WHERE character = %s
        """
        self.cursor.execute(query, (
            entry.name,
            entry.type.name,
            entry.symbol
        ))
        self.connection.commit()

    def delete_character(self, symbol: str) -> None:
        query = "DELETE FROM devanagari_characters WHERE character = %s"
        self.cursor.execute(query, (symbol,))
        self.connection.commit()

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
            pronunciation=''  # Assuming pronunciation is not stored in the database
        ) for row in results]