from erori.exceptions import RepositoryError, ValidationError
from validare.validators import ValidatorFilm
from domain.entities import Film
class RepoFilme(object):
    def __init__(self):
        self._filme = {}
    def set_filme(self, value):
        self._filme = value
    def get_filme(self):
        return self._filme
    def get_filme_idx(self,idx):
        return self._filme[idx]
    def size (self):
        return len(self._filme)
    def sterge (self, idx):
        self._filme.pop(idx)
    def delete_by_id(self, idx):
        if idx in self._filme:
            self._filme.pop(idx)
        else:
            raise RepositoryError("Id-ul nu exista!")
    def search_nume(self, nume, idx):
        if self._filme[idx].get_nume() == nume:
            return True
        return False
    def store (self, film):
        if film.get_id_film() in self._filme:
            raise RepositoryError("Acest id exista deja!")
        else:
            self._filme[film.get_id_film()]= film
    def modifica(self, original, id_film, nume, pret):
        filmval = Film(id_film, nume, pret)
        valid = ValidatorFilm()
        try:
            valid.validate(filmval)
        except ValidationError as ve:
            print (str(ve))
            return -1
        self.get_filme_idx(original).set_nume(nume)
        self.get_filme_idx(original).set_pret(pret)
        self.get_filme_idx(original).set_id(id_film)
        self.get_filme()[id_film] = self.get_filme().pop(original)
        
class RepoClienti(object):
    def __init__(self):
        self._clienti = []
    def get_clienti(self):
        return self._clienti
    def get_client_dupa_id(self, id_client):
        for x in self._clienti:
            if x.get_id_client() == id_client:
                return x
        
    def store (self, client):
        if any(x.get_id_client() == client.get_id_client() for x in self.get_clienti()):
            raise RepositoryError("Acest id exista deja!")
        
        if any(x.get_cnp() == client.get_cnp() for x in self.get_clienti()):
            raise RepositoryError("Acest CNP exista deja!")
        
        self.get_clienti().append(client)
    
    def lungime(self):
        return len(self.get_clienti())
    def get_all(self):
        return self._clienti[:]
    def search_nume(self, nume, idx):
        if idx.get_nume() == nume:
            return True
        return False
    def delete_client(self, id_client):
        if any(x.get_id_client() == id_client for x in self.get_clienti()):
            for client in self.get_clienti():
                if client.get_id_client() == id_client:
                    self._clienti.remove(client)
                    return
        else: 
            raise RepositoryError("Id-ul nu exista!")
    def modifica_client(self, client):
        self.store(client)      
   
class RepoRent (object):
    def __init__(self):
        self._rents = {}
    def store (self, rent):
        if rent.get_id_rent() in self._rents:
            raise RepositoryError("Id-ul exista deja!")
        else:
            self._rents[rent.get_id_rent()]=rent
    def size (self):
        return len(self._rents)
    def sterge (self, id_stergere_rent):
        try:
            self._rents.pop(id_stergere_rent)
        except KeyError:
            raise RepositoryError("Acest ID nu exista!")
    def returneaza_film (self, id_rent):
        try:
            self._rents[id_rent].returnare()
        except KeyError:
            raise RepositoryError("Acest ID nu exista!")
    def get_rent(self, id_rent):
        try:
            return self._rents[id_rent]
        except KeyError:
            raise RepositoryError("Acest ID nu exista!")
    def get_all_rents(self, idx=0):
        # return list(self._rents.values()) - NON-RECUSRIV
        # Creeaza recursiv lista returnata
        rentss = list(self._rents.values())
        if idx < len(rentss) - 1:
            return [rentss[idx]] + self.get_all_rents(idx=idx+1)
        else:
            return [rentss[idx]]

        
        
