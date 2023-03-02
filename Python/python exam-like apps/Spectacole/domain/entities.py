class Spectacol(object):
    def __init__(self, titlu, artist, gen, durata):
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__durata = durata

    def get_titlu(self):
        return self.__titlu


    def get_artist(self):
        return self.__artist


    def get_gen(self):
        return self.__gen


    def get_durata(self):
        return self.__durata


    def set_titlu(self, value):
        self.__titlu = value


    def set_artist(self, value):
        self.__artist = value


    def set_gen(self, value):
        self.__gen = value


    def set_durata(self, value):
        self.__durata = value
    
    def __str__(self):
        return f'<{self.get_titlu()}> || {self.get_artist()} || {self.get_gen()} || {self.get_durata()}'
    #def __repr__(self):
    #    return f'<{self.get_titlu()}> || {self.get_artist()} || {self.get_gen()} || {self.get_durata()}'


