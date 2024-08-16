from abc import ABC, abstractmethod
from typing import Optional, List
from model.lexical_entry import LexicalEntry
from model.word import Word

class Repository(ABC):
    @abstractmethod
    def get_character(self, symbol: str) -> Optional[LexicalEntry]:
        pass

    @abstractmethod
    def get_all_characters(self) -> List[LexicalEntry]:
        pass

    @abstractmethod
    def add_character(self, entry: LexicalEntry) -> None:
        pass

    @abstractmethod
    def get_word(self, word_form: str) -> Optional[Word]:
        pass

    @abstractmethod
    def add_word(self, word: Word) -> None:
        pass