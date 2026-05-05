from popups import *



class LanguageCenter:
    def __init__(self):
        self.lang = None


    def set_language(self):
        self.lang = self.choose_language()
        print(self.lang)
        return self.lang


    def choose_language(self):
        pass