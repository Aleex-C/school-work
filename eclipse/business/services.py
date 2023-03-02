from domain.entities import Film, Client, Rent
from erori.exceptions import RepositoryError, ValidationError
from sortare.sortari import MergeSorter

class ServiceFilme(object):
    def __init__(self, valid_film, repo_filme):
        self.__valid_film = valid_film
        self.__repo_filme = repo_filme
    
    def add_film(self, id_film, nume, pret):
        film = Film(id_film, nume, pret)
        self.__valid_film.validate(film)
        self.__repo_filme.store(film)
       
    
    def srv_search_nume (self, nume, idx=0):
        rez = []
        for film in self.__repo_filme.get_filme().values():
            if film.get_nume()==nume:
                rez.append(film.get_id_film())
        if len(rez)==0:
            return -1
        else: 
            return rez
              
    def delete_film (self, nume):
        idx_stergere = self.srv_search_nume(nume)
        if idx_stergere == -1:
            return -1
        for idx in idx_stergere:
            if idx_stergere != None:
                self.__repo_filme.sterge(idx)
            else:
                return -1
    def delete_film_by_id(self, idx_stergerex):
        self.__repo_filme.delete_by_id(idx_stergerex)
    def len_filme(self):
        return self.__repo_filme.size()
    
    def srv_get_film (self):
        return self.__repo_filme.get_filme()
    
    def afisare_idx(self, idx):
        return self.__repo_filme.get_filme_idx(idx)
    
    def sortare_dupa_id(self):
        sorter = MergeSorter()
        lista = list(self.__repo_filme.get_filme().items())
        sorter.sort(lista, key=lambda x: (x[1].get_nume(), x[1].get_pret()))
        d1 = dict(lista)
        self.__repo_filme.set_filme(d1)
        self.__repo_filme.write_all_to_file()
        
    def modifica (self, original, id_film, nume, pret):
        if self.__repo_filme.modifica(original, id_film, nume, pret) == -1:
            return -1
class ServiceClienti(object):
    def __init__(self, valid_client, repo_clienti):
        self.__valid_client = valid_client
        self.__repo_clienti = repo_clienti
    def add_client (self, id_client, nume, cnp):
        client = Client(id_client, nume, cnp)
        self.__valid_client.validate(client)
        self.__repo_clienti.store(client)
    def get_clienti (self):
        return self.__repo_clienti.get_clienti()
    def get_all_clienti(self):
        return self.__repo_clienti.get_all()
    def get_client_dupa_id(self, id_client):
        return self.__repo_clienti.get_client_dupa_id(id_client)
    
    def srv_search_nume (self, nume):
        rez = []
        for client in self.__repo_clienti.get_clienti():
            if self.__repo_clienti.search_nume(nume, client) == True:
                rez.append(client.get_id_client())
        if len(rez)==0:
            return -1
        else:
            return rez
    def delete_id_client (self, id_client):
        self.__repo_clienti.delete_client(id_client)

    def modifica (self, original, id_client_nou, nume_nou, CNP_nou):
        client = Client(id_client_nou, nume_nou, CNP_nou)
        self.__valid_client.validate(client)
        aux = self.get_client_dupa_id(original)
        self.delete_id_client(original)
        try:
            self.__repo_clienti.modifica_client(client)
        except ValidationError as ve:
            self.__repo_clienti.modifica_client(aux)
            raise ValidationError(ve)
        except RepositoryError as re:
            self.__repo_clienti.modifica_client(aux)
            raise RepositoryError(re)
    def len_clienti(self):
        return self.__repo_clienti.lungime()
class ServiceRents(object):
    def __init__(self, valid_rent, repo_rents, repo_clienti, repo_filme):
        self.__repo_rents = repo_rents
        self.__repo_clienti = repo_clienti
        self.__repo_filme = repo_filme
        self.__valid_rent = valid_rent
    def len_rents (self):
        return self.__repo_rents.size()
    def creeaza_rent(self, id_rent, id_client, id_film):
        rent = Rent(id_rent, id_client, id_film)
        self.__valid_rent.validate(rent)
        if any(x.get_id_client() == id_client for x in self.__repo_clienti.get_clienti()) == False:
            raise ValidationError("Acest ID de client nu exista")
        if not id_film in self.__repo_filme.get_filme():
            raise ValidationError("Acest ID de film nu exista")
        if (self.__repo_rents.size()>0):
            for r in self.__repo_rents.get_all_rents():
                if (r.get_status()=="imprumutat" and r.get_id_film()==id_film):
                    raise ValidationError("Acest film este deja imprumutat!")
        self.__repo_rents.store(rent)
        return rent
    def returneaza_film (self, id_rent):
        self.__repo_rents.returneaza_film(id_rent)
    def sterge (self, id_rent):
        self.__repo_rents.sterge(id_rent)
    def get_all_rents(self):
        return self.__repo_rents.get_all_rents()
    def get_rent_id (self, idr):
        return self.__repo_rents.get_rent(idr)
    
    def get_clienti_sortat (self, ok=False):
        rents = self.__repo_rents.get_all_rents()
        ids_clienti = []
        for rent in rents:
            idc = rent.get_id_client()
            if ids_clienti.count(idc)==0:
                ids_clienti.append(idc)
        lista_nume = []
        for idc in ids_clienti:
            count = 0
            for rent in rents:
                if rent.get_id_client()==idc:
                    count += 1 
            if count > 0:
                lista_nume.append([self.__repo_clienti.get_client_dupa_id(idc).get_nume(), count])
        if ok == False:
            return sorted(lista_nume, key=lambda x: x[0])
        else:
            return sorted(lista_nume, key=lambda x: x[1], reverse=True)
    def get_filme_rents(self):
        sorter = MergeSorter()
        idfs = []
        rez = []
        all_idfs = []
        rents = self.__repo_rents.get_all_rents()
        for rent in rents:
            idf = rent.get_id_film()
            if idfs.count(idf)==0:
                idfs.append(idf)
                all_idfs.append(idf)
            elif idf in idfs:
                all_idfs.append(idf)
        for idf in idfs:
            count = all_idfs.count(idf)
            rez.append((self.__repo_filme.get_filme_idx(idf).get_nume(), count))
        
        sorter.sort(rez, key=lambda x: (x[1], x[0]), reverse=True)
        return rez
            

        
        
        
