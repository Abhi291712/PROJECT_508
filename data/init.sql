-- Create the main database
CREATE DATABASE IF NOT EXISTS devanagari;
ALTER DATABASE devanagari CHARACTER SET utf8 COLLATE utf8_unicode_ci;

-- Create the test database
CREATE DATABASE IF NOT EXISTS test_devanagari;
ALTER DATABASE test_devanagari CHARACTER SET utf8 COLLATE utf8_unicode_ci;

-- Create test user and grant privileges
CREATE USER IF NOT EXISTS 'test_user'@'%' IDENTIFIED BY 'test_password';
GRANT ALL PRIVILEGES ON test_devanagari.* TO 'test_user'@'%';
FLUSH PRIVILEGES;

-- Use the main database for the following operations
USE devanagari;

-- Create a table for Devanagari characters
CREATE TABLE IF NOT EXISTS devanagari_characters (
    id INT NOT NULL AUTO_INCREMENT,
    `character` VARCHAR(10) NOT NULL,
    name VARCHAR(50),
    type VARCHAR(20),
    PRIMARY KEY (id)
);

INSERT INTO devanagari_characters (character, name, type)
VALUES
    ('अ', 'A', 'Vowel'),
    ('आ', 'Ā', 'Vowel'),
    ('इ', 'I', 'Vowel'),
    ('ई', 'Ī', 'Vowel'),
    ('उ', 'U', 'Vowel'),
    ('ऊ', 'Ū', 'Vowel'),
    ('क', 'Ka', 'Consonant'),
    ('ख', 'Kha', 'Consonant'),
    ('ग', 'Ga', 'Consonant'),
    ('घ', 'Gha', 'Consonant'),
    ('च', 'Cha', 'Consonant'),
    ('छ', 'Chha', 'Consonant'),
    ('ज', 'Ja', 'Consonant'),
    ('झ', 'Jha', 'Consonant'),
    ('ट', 'ṭa', 'Consonant'),
    ('ठ', 'ṭha', 'Consonant'),
    ('ड', 'ḍa', 'Consonant'),
    ('ढ', 'ḍha', 'Consonant'),
    ('त', 'Ta', 'Consonant'),
    ('थ', 'Tha', 'Consonant'),
    ('द', 'Da', 'Consonant'),
    ('ध', 'Dha', 'Consonant'),
    ('प', 'Pa', 'Consonant'),
    ('फ', 'Pha', 'Consonant'),
    ('ब', 'Ba', 'Consonant'),
    ('भ', 'Bha', 'Consonant'),
    ('म', 'Ma', 'Consonant'),
    ('य', 'Ya', 'Consonant'),
    ('र', 'Ra', 'Consonant'),
    ('ल', 'La', 'Consonant'),
    ('व', 'Va', 'Consonant'),
    ('श', 'Sha', 'Consonant'),
    ('ष', 'Ṣa', 'Consonant'),
    ('स', 'Sa', 'Consonant'),
    ('ह', 'Ha', 'Consonant');

-- Create a table for words
CREATE TABLE IF NOT EXISTS words (
    id INT NOT NULL AUTO_INCREMENT,
    devanagari_word NVARCHAR(100) NOT NULL,
    latin_transliteration VARCHAR(100),
    PRIMARY KEY (id)
);

-- Insert sample data into words
INSERT INTO words (devanagari_word, latin_transliteration)
VALUES
    ('नमस्ते', 'namaste'),
    ('धन्यवाद', 'dhanyavaad'),
    ('भारत', 'Bharat'),
    ('शक्ति', 'Shakti'),
    ('शिव', 'Shiva'),
    ('ज्ञान', 'Gyaan'),
    ('आत्मा', 'Atma'),
    ('योग', 'Yoga'),
    ('सत्य', 'Satya'),
    ('अद्वितीय', 'Advitiya');

-- Now set up the test database
USE test_devanagari;

-- Create the same tables in the test database
CREATE TABLE IF NOT EXISTS devanagari_characters (
    id INT NOT NULL AUTO_INCREMENT,
    `character` VARCHAR(10) NOT NULL,
    name VARCHAR(50),
    type VARCHAR(20),
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS words (
    id INT NOT NULL AUTO_INCREMENT,
    devanagari_word NVARCHAR(100) NOT NULL,
    latin_transliteration VARCHAR(100),
    PRIMARY KEY (id)
);