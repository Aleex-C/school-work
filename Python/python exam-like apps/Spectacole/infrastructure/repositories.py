import re
from domain.entities import Spectacol
from erroare.exceptii import RepositoryError
class RepoSpectacole(object):
    def __init__(self):
        self._spectacole = []
    def store (self, spectacol):
        self._spectacole.append(spectacol)
    def get_spectacole (self):
        return self._spectacole
    def size(self):
        return len(self._spectacole)
        
        
        

class RepoSpectacoleFile(RepoSpectacole):
    def __init__(self, file_path):
        self.__file_path = file_path
        self.__read_all_from_file()
    
    def __read_all_from_file(self):
        with open (self.__file_path, "rt") as f:
            lines = f.readlines()
            self._spectacole = []
            for line in lines:
                line = line.strip()
                #line = re.sub(' +', '', line)
                if len(line)>0:
                    parts = line.split(',')
                    titlu = parts[0]
                    artist = parts[1]
                    gen = parts[2]
                    durata = int(parts[3])
                    self._spectacole.append(Spectacol(titlu, artist, gen, durata))
    def __write_all_to_file(self):
        with open (self.__file_path, "wt") as f:
            for spectacol in self._spectacole:
                f.write(f'{spectacol.get_titlu()},{spectacol.get_artist()},{spectacol.get_gen()},{spectacol.get_durata()}\n')
    def __append_to_file(self):
        with open (self.__file_path, "a") as f:
            for spectacol in self._spectacole:
                f.write(f'{spectacol.get_titlu()},{spectacol.get_artist()},{spectacol.get_gen()},{spectacol.get_durata()}\n')
    def store(self, spectacol):
        self.__read_all_from_file()
        RepoSpectacole.store(self, spectacol)
        self.__write_all_to_file()
    def update(self, spectacol, gen_nou, durata_nou):
        self.__read_all_from_file()
        RepoSpectacole.update(self, spectacol, gen_nou, durata_nou)
        self.__write_all_to_file()
    def exportare (self, file_export, spec):
        with open(file_export, "w") as f:
            for spectacol in spec:
                f.write(f'{spectacol.get_artist()},{spectacol.get_titlu()},{spectacol.get_durata()},{spectacol.get_gen()}\n')
                
