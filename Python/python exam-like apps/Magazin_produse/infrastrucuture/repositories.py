from errors.exceptii import RepositoryError
import re
from entities.produs import Produs
class RepoProduse(object):
    def __init__(self):
        self._produse = {}

    def get_produse(self):
        return self._produse.values()
    def size(self):
        return len(self._produse)
    def store(self, produs):
        if produs.get_id_produs() in self._produse:
            raise RepositoryError("Acest ID exsita deja!")
        else:
            self._produse[produs.get_id_produs()]=produs
    def delete(self, id_remove):
        try:
            self._produse.pop(id_remove)
        except KeyError:
            raise RepositoryError("Acest id nu exista!")
            
class RepoProduseFile(RepoProduse):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_all_from_file()
    def __read_all_from_file(self):
        with open(self.__file_path, "rt") as f:
            lines = f.readlines()
            self._produse = {}
            for line in lines:
                line = line.strip()
                line = re.sub(' +', '', line)
                if len(line)>0:
                    parts = line.split(',')
                    id_produs = int(parts[0])
                    denumire = parts[1]
                    pret = int(parts[2])
                self._produse[id_produs]=Produs(id_produs, denumire, pret)
    def __write_all_to_file(self):
        with open(self.__file_path, "wt") as f:
            for produs in self._produse.values():
                f.write(f'{produs.get_id_produs()},{produs.get_denumire()},{produs.get_pret()}\n')
    def __append_to_file(self):
        with open(self.__file_path, "a") as f:
            for produs in self._produse.values():
                f.write(f'{produs.get_id_produs()},{produs.get_denumire()},{produs.get_pret()}\n')
    def store(self, produs):
        self.__read_all_from_file()
        RepoProduse.store(self, produs)
        self.__write_all_to_file()
    def delete(self, id_remove):
        self.__read_all_from_file()
        RepoProduse.delete(self, id_remove)
        self.__write_all_to_file()
        


