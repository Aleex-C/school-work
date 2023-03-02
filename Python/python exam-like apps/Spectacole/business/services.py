from domain.entities import Spectacol
import random
from string import ascii_lowercase
import string
class ServiceSpectacole(object):
    def __init__(self, repo_spec, valid_spec):
        self.__repo_spec = repo_spec
        self.__valid_spec = valid_spec
    def adauga_spectacol (self, titlu, artist, gen, durata):
        spectacol = Spectacol(titlu, artist, gen, durata)
        self.__valid_spec.validate(spectacol)
        self.__repo_spec.store(spectacol)
    def get_all_spectacole(self):
        return self.__repo_spec.get_spectacole()
    def generare_spectacole(self, nr):
        lista_genuri = ["comedie", "concert", "balet", "altele"]
        vocale = "aeiou"
        consoane = "bcdfghjklmnpqrstvxyz"
        char = (consoane, vocale)
        for j in range(0,nr):
            size = random.randint(9,12)
            mid = size//2
            titlu = ''.join(random.choice(char[i%2]) for i in range(size))
            t1 = titlu[:mid]
            t2 = titlu[mid:]
            titlu = t1+ " " + t2
            artist = ''.join(random.choice(char[i%2]) for i in range(size))
            t1 = artist[:mid]
            t2 = artist[mid:]
            artist = t1+ " " + t2
            gen = random.choice(lista_genuri)
            durata = random.randint(1, 1000000)
            self.adauga_spectacol(titlu, artist, gen, durata)
            print(Spectacol(titlu, artist, gen, durata))
    def export (self, file_export):
        spectacole = self.get_all_spectacole()
        spectacole_sortat = sorted(spectacole, key=lambda x: (x.get_artist(),x.get_titlu()), reverse=False)
        self.__repo_spec.exportare(file_export, spectacole_sortat)
        


