from abc import ABC, abstractmethod
from typing import Optional
from model.lexical_entry import LexicalEntry

class Repository(ABC):
    @abstractmethod
    def add_character(self, entry: LexicalEntry) -> None:
        pass

    @abstractmethod
    def get_character(self, symbol: str) -> Optional[LexicalEntry]:
        pass

    @abstractmethod
    def update_character(self, entry: LexicalEntry) -> None:
        pass

    @abstractmethod
    def delete_character(self, symbol: str) -> None:
        pass

    @abstractmethod
    def add_word_transliteration(self, word: str, transliteration: str) -> None:
        pass

    @abstractmethod
    def get_word_transliteration(self, word: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_all_characters(self) -> list:
        pass