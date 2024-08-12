import unittest
from db.mysql_repository import MysqlRepository
from model.lexical_entry import LexicalEntry, CharacterType


class TestMySQLRepository(unittest.TestCase):
    def setUp(self):
        # Use a test database
        self.repo = MysqlRepository(
            host="localhost",  # Use "db" if running tests inside Docker
            user="test_user",
            password="test_password",
            database="test_devanagari"
        )

    def tearDown(self):
        # Clean up the test database after each test
        self.repo.cursor.execute("DELETE FROM devanagari_characters")
        self.repo.cursor.execute("DELETE FROM words")
        self.repo.connection.commit()

    def test_add_and_get_character(self):
        entry = LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/")
        self.repo.add_character(entry)

        retrieved = self.repo.get_character("अ")
        self.assertIsNotNone(retrieved)
        self.assertEqual(retrieved.symbol, "अ")
        self.assertEqual(retrieved.name, "a")
        self.assertEqual(retrieved.type, CharacterType.VOWEL)

    def test_update_character(self):
        entry = LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/")
        self.repo.add_character(entry)

        updated_entry = LexicalEntry("अ", "aa", CharacterType.VOWEL, "/aa/")
        self.repo.update_character(updated_entry)

        retrieved = self.repo.get_character("अ")
        self.assertEqual(retrieved.name, "aa")

    def test_delete_character(self):
        entry = LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/")
        self.repo.add_character(entry)

        self.repo.delete_character("अ")

        retrieved = self.repo.get_character("अ")
        self.assertIsNone(retrieved)

    def test_add_and_get_word_transliteration(self):
        self.repo.add_word_transliteration("नमस्ते", "namaste")

        transliteration = self.repo.get_word_transliteration("नमस्ते")
        self.assertEqual(transliteration, "namaste")

    def test_get_all_characters(self):
        entries = [
            LexicalEntry("अ", "a", CharacterType.VOWEL, "/a/"),
            LexicalEntry("क", "ka", CharacterType.CONSONANT, "/ka/")
        ]
        for entry in entries:
            self.repo.add_character(entry)

        all_chars = self.repo.get_all_characters()
        self.assertEqual(len(all_chars), 2)
        self.assertEqual(all_chars[0].symbol, "अ")
        self.assertEqual(all_chars[1].symbol, "क")


if __name__ == '__main__':
    unittest.main()