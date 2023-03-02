import re
from domain.entities import Elicopter
class RepoElicopter():
    def __init__ (self):
        self._elicoptere = {}
    def get_all(self):
        return list(self._elicoptere.values())


class RepoElicopterFile(RepoElicopter):
    def __init__(self, file_path):
        RepoElicopter.__init__(self)
        self.__file_path = file_path
        self.__read_all_from_file()
    def __read_all_from_file(self):
        with open(self.__file_path,"rt") as f:
            self._elicoptere = {}
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = re.sub(' +','',line)
                if len(line)>0:
                    parts = line.split(',')
                    try:
                        id_heli = int(parts[0])
                        year = int(parts[3])
                    except ValueError:
                        continue
                    name = parts[1]
                    scop = parts[2]
                    if (id_heli>0 and year>0 and name!="" and scop!="" and len(parts)==4):
                        self._elicoptere[id_heli]=Elicopter(id_heli, name, scop, year)
                    
                    


