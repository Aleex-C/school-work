class Elicopter(object):
    def __init__(self, id_heli, name, scop, year):
        self.__id_heli = id_heli
        self.__name = name
        self.__scop = scop
        self.__year = year

    def get_id_heli(self):
        return self.__id_heli


    def get_name(self):
        return self.__name


    def get_scop(self):
        return self.__scop


    def get_year(self):
        return self.__year
    def __str__(self):
        return f'<{self.__id_heli}> {self.__name} || {self.__scop} -> {self.__year}'
    


