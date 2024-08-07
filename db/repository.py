from abc import ABC, abstractmethod
from typing import List, Optional
from model.lexical_entry import LexicalEntry

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
    def get_word_transliteration(self, word: str) -> Optional[str]:
        pass

    @abstractmethod
    def add_word_transliteration(self, word: str, transliteration: str) -> None:
        pass
