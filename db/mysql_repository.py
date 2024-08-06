import mysql.connector
import os
from typing import List, Optional
from db.repository import Repository
from model.lexical_entry import LexicalEntry, Translation
from model.common_enums import CharacterType



    def get_character(self, symbol: str) -> Optional[LexicalEntry]:
        query = "SELECT * FROM devanagari_characters WHERE character = %s"
        self.cursor.execute(query, (symbol,))
        result = self.cursor.fetchone()
        if result:
            return LexicalEntry(
                symbol=result['character'],
                name=result['name'],
                type=CharacterType[result['type']],
                pronunciation='',  # Adjust as necessary if 'pronunciation' is part of your model
                translation=Translation('', '')  # Adjust as necessary if 'translation' is part of your model
            )
        return None

    def get_all_characters(self) -> List[LexicalEntry]:
        query = "SELECT * FROM devanagari_characters"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        return [
            LexicalEntry(
                symbol=row['character'],
                name=row['name'],
                type=CharacterType[row['type']],
                pronunciation='',  # Adjust as necessary
                translation=Translation('', '')  # Adjust as necessary
            )
            for row in results
        ]

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

    def get_word_transliteration(self, word: str) -> Optional[str]:
        query = "SELECT latin_transliteration FROM words WHERE devanagari_word = %s"
        self.cursor.execute(query, (word,))
        result = self.cursor.fetchone()
        return result['latin_transliteration'] if result else None

    def add_word_transliteration(self, word: str, transliteration: str) -> None:
        query = "INSERT INTO words (devanagari_word, latin_transliteration) VALUES (%s, %s)"
        self.cursor.execute(query, (word, transliteration))
        self.connection.commit()

    def __del__(self):
        if hasattr(self, 'connection') and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
