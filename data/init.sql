-- Create the main database
CREATE DATABASE IF NOT EXISTS devanagari;
USE devanagari;

-- Create a table for Devanagari characters
CREATE TABLE IF NOT EXISTS devanagari_characters (
    id INT NOT NULL AUTO_INCREMENT,
    symbol VARCHAR(10) NOT NULL,
    name VARCHAR(50),
    type VARCHAR(20),
    pronunciation VARCHAR(100),
    PRIMARY KEY (id)
);

-- Insert sample data into devanagari_characters
INSERT INTO devanagari_characters (symbol, name, type, pronunciation) VALUES
    ('अ', 'a', 'VOWEL', '/a/ (''a'' in ''about'')'),
    ('आ', 'ā', 'VOWEL', '/ɑː/ (''a'' in ''father'')'),
    ('क', 'ka', 'CONSONANT', '/kə/ (''k'' in ''kite'')'),
    ('ख', 'kha', 'CONSONANT', '/kʰə/ (aspirated ''k'' in ''khaki'')');

-- Create a table for words
CREATE TABLE IF NOT EXISTS words (
    id INT NOT NULL AUTO_INCREMENT,
    word_form VARCHAR(100) NOT NULL,
    pronunciation VARCHAR(100),
    transliteration VARCHAR(100),
    PRIMARY KEY (id)
);

-- Insert sample data into words
INSERT INTO words (word_form, pronunciation, transliteration) VALUES
    ('नमस्ते', 'namaste', 'namaste'),
    ('धन्यवाद', 'dhanyavaad', 'dhanyavaad');