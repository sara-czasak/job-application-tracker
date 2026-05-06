from popups import *
from languages import languages



class LanguageCenter:
    def __init__(self, lang):
        self.lang = lang
        self.dictionary = languages

    def set_language(self):
        print(self.lang)
        return self.lang


    def translate(self, text):
        if self.lang:
            translated_text = self.dictionary[self.lang][text]
            return translated_text
        else:
            return None