from typing import Dict, Optional
from model.common_enums import CharacterType
from model.lexical_entry import LexicalEntry, Translation

class CharacterIdentifier:
    def __init__(self):
        self.char_info: Dict[str, LexicalEntry] = {
            "अ": LexicalEntry("अ", "a", CharacterType.VOWEL, "/ə/", Translation("a", "The first letter of the Devanagari script")),
            # Add more characters here
        }

    def identify(self, char: str) -> Optional[LexicalEntry]:
        return self.char_info.get(char)
