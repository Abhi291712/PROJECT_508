import mysql.connector
from typing import Optional, List
from model.lexical_entry import LexicalEntry, CharacterType
from model.word import Word
from db.repository import Repository

class MysqlRepository(Repository):
    def __init__(self, host: str, user: str, password: str, database: str, port: int = 3306):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        self.cursor = self.connection.cursor(dictionary=True)

    def get_character(self, symbol: str) -> Optional[LexicalEntry]:
        query = "SELECT * FROM devanagari_characters WHERE symbol = %s"
        self.cursor.execute(query, (symbol,))
        result = self.cursor.fetchone()
        if result:
            return LexicalEntry(
                symbol=result['symbol'],
                name=result['name'],
                type=CharacterType[result['type'].upper()],
                pronunciation=result['pronunciation']
            )
        return None

    def get_all_characters(self) -> List[LexicalEntry]:
        query = "SELECT * FROM devanagari_characters"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [LexicalEntry(
            symbol=row['symbol'],
            name=row['name'],
            type=CharacterType[row['type'].upper()],
            pronunciation=row['pronunciation']
        ) for row in results]

    def add_character(self, entry: LexicalEntry) -> None:
        query = "INSERT INTO devanagari_characters (symbol, name, type, pronunciation) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (entry.symbol, entry.name, entry.type.name, entry.pronunciation))
        self.connection.commit()

    def get_word(self, word_form: str) -> Optional[Word]:
        query = "SELECT * FROM words WHERE word_form = %s"
        self.cursor.execute(query, (word_form,))
        result = self.cursor.fetchone()
        if result:
            return Word(
                word_form=result['word_form'],
                pronunciation=result['pronunciation'],
                transliteration=result['transliteration']
            )
        return None

    def add_word(self, word: Word) -> None:
        query = "INSERT INTO words (word_form, pronunciation, transliteration) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (word.word_form, word.pronunciation, word.transliteration))
        self.connection.commit()