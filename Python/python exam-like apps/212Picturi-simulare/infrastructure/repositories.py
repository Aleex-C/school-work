from errors.erori import RepositoryError
import re
from domain.entities import Pictura

class RepoPicturi(object):
    def __init__(self):
        self._picturi = {}
    def store (self, pic):
        if pic.get_id_pic() in self._picturi:
            raise RepositoryError("Acest ID exsita deja!")
        else:
            self._picturi[pic.get_id_pic()] = pic
    def size (self):
        return len(self._picturi)
    def sterge (self, id_pic):
        try:
            self._picturi.pop(id_pic)
        except KeyError:
            raise RepositoryError("Acest ID nu exista!")
    def get_pic(self, id_pic):
        try:
            return self._picturi[id_pic]
        except KeyError:
            raise RepositoryError("Acest ID nu exista!")
    def get_all_pics (self):
        return list(self._picturi.values())
class RepoPicturiFile (RepoPicturi):
    def __init__ (self, file_name):
        RepoPicturi.__init__(self)
        self.__file_name = file_name
        self.__read_all_from_file()
    def __read_all_from_file (self):
        with open(self.__file_name, "rt") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = re.sub(' +','', line)
                if len(line)>0:
                    parts = line.split(',')
                    try:
                        id_pic = int(parts[0])
                        year = int(parts[3])
                    except ValueError:
                        continue
                    pic_name = parts[1]
                    author_name = parts[2]
                    if (id_pic>0 and year>0 and pic_name!="" and author_name!="" and len(parts)==4):
                        self._picturi[id_pic]=Pictura(id_pic, pic_name, author_name, year)
                    

