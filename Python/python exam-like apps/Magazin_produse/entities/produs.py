class Produs(object):
    def __init__(self, id_produs, denumire, pret):
        self.__id_produs = id_produs
        self.__denumire = denumire
        self.__pret = pret

    def get_id_produs(self):
        return self.__id_produs


    def get_denumire(self):
        return self.__denumire


    def get_pret(self):
        return self.__pret


    def set_id_produs(self, value):
        self.__id_produs = value


    def set_denumire(self, value):
        self.__denumire = value


    def set_pret(self, value):
        self.__pret = value
    
    def __repr__(self, *args, **kwargs):
        return f'<{str(self.__id_produs)}> || {self.__denumire} -> {self.__pret}'   
    def __str__(self):
        return f'<{str(self.__id_produs)}> || {self.__denumire} -> {self.__pret}'

    
        


