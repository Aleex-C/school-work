from domain.entities import Concurent, Participare
import re

class RepoConcurenti(object):
    def __init__(self):
        self._concurenti = {}
    def get_all(self):
        return list(self._concurenti.values())
    def get_by_id(self, id_cautat):
        try:
            return self._concurenti[id_cautat]
        except KeyError:
            raise Exception("Acest ID nu exista!")

class RepoConcurentiFile(RepoConcurenti):
    
    def __init__(self, file_path):
        RepoConcurenti.__init__(self)
        self.__file_path = file_path
        self.__read_all_from_file()
 
    def __read_all_from_file(self):
        with open(self.__file_path,"rt") as f:
            self._concurenti = {}
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = re.sub(' +','',line)
                if len(line)>0:
                    parts = line.split(',')
                    id_concurent = parts[0]
                    nume = parts[1]
                    tara = parts[2]
                    data_nasterii=parts[3]
                    self._concurenti[id_concurent]=Concurent(id_concurent, nume, tara, data_nasterii)
    

class RepoParticipari(object):
    def __init__(self):
        self._participari = {}
    def get_all(self):
        return list(self._participari.values())
    
class RepoParticipariFile(RepoParticipari):
    def __init__(self, file_path):
        RepoParticipari.__init__(self)
        self.__file_path = file_path
        self.__read_all_from_file()
 
    def __read_all_from_file(self):
        with open(self.__file_path,"rt") as f:
            self._participari = {}
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = re.sub(' +','',line)
                if len(line)>0:
                    parts = line.split(',')
                    cod_p = parts[0]
                    id_c = parts[1]
                    punctaj = parts[2]
                    self._participari[cod_p]=Participare(cod_p, id_c, punctaj)


