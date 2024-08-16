class Word:
    def __init__(self, word_form, pronunciation=None, transliteration=None):
        self.word_form = word_form
        self.pronunciation = pronunciation
        self.transliteration = transliteration

    def __repr__(self):
        return f"Word(word_form={self.word_form}, pronunciation={self.pronunciation}, transliteration={self.transliteration})"