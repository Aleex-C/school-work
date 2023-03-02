class Pictura(object):
    def __init__ (self, id_pic, pic_name, author_name, year):
        self.__id_pic = id_pic
        self.__pic_name = pic_name
        self.__author_name = author_name
        self.__year = year

    def get_id_pic(self):
        return self.__id_pic


    def get_pic_name(self):
        return self.__pic_name


    def get_author_name(self):
        return self.__author_name


    def get_year(self):
        return self.__year
    def __str__(self):
        return f'<{self.__id_pic}> {self.__pic_name} || {self.__author_name} -> {self.__year}'
        


