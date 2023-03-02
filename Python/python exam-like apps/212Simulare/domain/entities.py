class Concurent(object):
    def __init__(self, id_concurent, nume, tara, data_nasterii):
        self.__id_concurent = id_concurent
        self.__nume = nume
        self.__tara = tara
        self.__data_nasterii = data_nasterii

    def get_id_concurent(self):
        return self.__id_concurent


    def get_nume(self):
        return self.__nume


    def get_tara(self):
        return self.__tara


    def get_data_nasterii(self):
        return self.__data_nasterii
    def __str__(self):
        return f'<{self.__id_concurent}> {self.__nume} || {self.__tara} || {self.__data_nasterii}'

class Participare(object):
    def __init__(self,cod_p, id_c, punctaj):
        self.__cod_p = cod_p
        self.__id_c = id_c
        self.__punctaj = punctaj

    def get_cod_p(self):
        return self.__cod_p


    def get_id_c(self):
        return self.__id_c


    def get_punctaj(self):
        return self.__punctaj
    def __str__(self):
        return f'[{self.__cod_p}] {self.__id_c} || {self.__punctaj}'


        
                


