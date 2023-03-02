from domain.entities import Client, Film, Rent
from infrastructura.repositories import RepoFilme, RepoClienti, RepoRent
import re

class RepoFilmeFile(RepoFilme):
    def __init__ (self, file_path):
        RepoFilme.__init__(self)
        self.__file_path = file_path
        self.read_all_from_file()
    def read_all_from_file(self):
        with open(self.__file_path, "rt") as f:
            lines = f.readlines()
            self._filme = {}
            for line in lines:
                line = line.strip()
                line = re.sub(' +', '', line)
                if len(line)>0:
                    parts = line.split(',')
                    id_film = int(parts[0])
                    nume_film = parts[1]
                    pret = int(parts[2])
                self._filme[id_film]=Film(id_film, nume_film, pret)
    def write_all_to_file(self):
        with open(self.__file_path, "wt") as f:
            for film in self._filme.values():
                f.write(f'{str(film.get_id_film())},{film.get_nume()},{str(film.get_pret())}\n')
    def append_to_file(self, film):
        with open(self.__file_path, "a") as f:
                f.write(f'{str(film.get_id_film())},{film.get_nume()},{str(film.get_pret())}\n')
    def store (self, film):
        self.read_all_from_file()
        RepoFilme.store(self, film)
        self.append_to_file(film)
    def delete_by_id (self, id_film):
        self.read_all_from_file()
        RepoFilme.delete_by_id(self, id_film)
        self.write_all_to_file()
    def modifica (self, original, id_nou, nume_nou, pret_nou):
        self.read_all_from_file()
        RepoFilme.modifica(self, original, id_nou, nume_nou, pret_nou)
        self.write_all_to_file()
class RepoClientiFile(RepoClienti):
    def __init__ (self, file_path):
        RepoClienti.__init__(self)
        self.__file_path = file_path
        self.read_all_from_file()
    '''
    def read_all_from_file(self):
        with open(self.__file_path, "rt") as f:
            lines = f.readlines()
            self._clienti = []
            for line in lines:
                line = line.strip()
                line = re.sub(' +', '', line)
                if len(line)>0:
                    parts = line.split(',')
                    id_client = int(parts[0])
                    nume_client = parts[1]
                    cnp = int(parts[2])
                self._clienti.append(Client(id_client, nume_client, cnp))
                
    def write_all_to_file(self):
        with open(self.__file_path, "wt") as f:
            for client in self._clienti:
                f.write(f'{str(client.get_id_client())},{client.get_nume()},{str(client.get_cnp())}\n')
    def append_to_file(self, client):
        with open(self.__file_path, "a") as f:
                f.write(f'{str(client.get_id_client())},{client.get_nume()},{str(client.get_cnp())}\n')
    '''
    def read_all_from_file(self):
        with open(self.__file_path, "rt") as f:
            lines = f.readlines()
            self._clienti = []
            idx = 0
            for line in lines:
                line = line.strip()
                line = re.sub(' +', '', line)
                if len(line)>0:
                    if idx%3==0:
                        id_client=int(line)
                    elif idx%3==1:
                        nume_client = str(line)
                    elif idx%3==2:
                        cnp = int(line)
                idx += 1
                if (idx%3==0 and idx!=0):
                    self._clienti.append(Client(id_client, nume_client, cnp))
    def write_all_to_file(self):
        with open(self.__file_path, "wt") as f:
            for client in self._clienti:
                f.write(f'{str(client.get_id_client())}\n{client.get_nume()}\n{str(client.get_cnp())}\n')
    def append_to_file(self, client):
        with open(self.__file_path, "a") as f:
            f.write(f'{str(client.get_id_client())}\n{client.get_nume()}\n{str(client.get_cnp())}\n')
    def store (self, client):
        self.read_all_from_file()
        RepoClienti.store(self, client)
        self.append_to_file(client)
    def delete_client (self, id_client):
        self.read_all_from_file()
        RepoClienti.delete_client(self, id_client)
        self.write_all_to_file()
    def modifica_client (self, client):
        self.read_all_from_file()
        RepoClienti.modifica_client(self, client)
        self.write_all_to_file()
class RepoRentsFile (RepoRent):
    def __init__ (self, file_path):
        RepoRent.__init__(self)
        self.__file_path = file_path
        self.read_all_from_file()
    def read_all_from_file(self):
        with open(self.__file_path, "rt") as f:
            lines = f.readlines()
            self._rents = {}
            for line in lines:
                line = line.strip()
                line = re.sub(' +', '', line)
                if len(line)>0:
                    parts = line.split(',')
                    id_rent = int(parts[0])
                    id_client = int(parts[1])
                    id_film = int(parts[2])
                self._rents[id_rent]=Rent(id_rent, id_client, id_film)
                if len(parts)>3:
                    if parts[3]=="returnat":
                        RepoRent.returneaza_film(self, id_rent)
    def append_to_file (self, rent):
        with open(self.__file_path, "a") as f:
            f.write(f'{str(rent.get_id_rent())},{str(rent.get_id_client())}, {str(rent.get_id_film())}, {rent.get_status()}\n')
    def write_all_to_file (self):
        with open(self.__file_path, "wt") as f:
            for rent in self._rents.values():
                f.write(f'{str(rent.get_id_rent())},{str(rent.get_id_client())}, {str(rent.get_id_film())}, {rent.get_status()}\n')
    def store(self, rent):
        self.read_all_from_file()
        RepoRent.store(self, rent)
        self.append_to_file(rent)
    def sterge (self, idx):
        self.read_all_from_file()
        RepoRent.sterge(self, idx)
        self.write_all_to_file()
    def returneaza_film(self, id_rent):
        self.read_all_from_file()
        RepoRent.returneaza_film(self, id_rent)
        self.write_all_to_file()
        