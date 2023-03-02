from business.services import ServiceFilme, ServiceClienti, ServiceRents
from infrastructura.repositories import RepoFilme, RepoClienti, RepoRent
from validare.validators import ValidatorFilm, ValidatorClient, ValidatorRent
from erori.exceptions import ValidationError, RepositoryError
from domain.entities import Film, Client
from infrastructura.file_repositories import RepoFilmeFile

class Teste (object):
    def __add_film_test(self):
        id_film = 23
        nume = "Godfather"
        pret = 999
        valid_film = ValidatorFilm()
        repo_filme = RepoFilme()
        srv_filme = ServiceFilme(valid_film, repo_filme)
        srv_filme.add_film(id_film, nume,pret)
        assert(srv_filme.len_filme()==1)
        bad_id_film = -23
        bad_nume = ""
        bad_pret = -999
        try:
            srv_filme.add_film(bad_id_film, nume, pret)
            assert False
        except ValidationError as ex:
            assert(str(ex)=="id invalid!")

        try:
            srv_filme.add_film(1, bad_nume, pret)
            assert False
        except ValidationError as ex:
            assert(str(ex)=="nume invalid!")

        try:
            srv_filme.add_film(2, nume, bad_pret)
            assert False
        except ValidationError as ex:
            assert(str(ex)=="pret invalid!")

    def __creeaza_film_test(self):
        film = Film(23, "Godfather", 999)
        assert (film.get_id_film()==23)
        assert (film.get_nume()=="Godfather")
        assert (film.get_pret()==999)
    def testValidatorFilm(self):
        val = ValidatorFilm()
        film = Film(-11, "", 22)
        try:
            val.validate(film)
            assert False
        except ValidationError:
            assert True
        film = Film (23, "Ion", -100)
        try:
            val.validate(film)
            assert False
        except ValidationError:
            assert True
    def testStoreFilm(self):
        val = ValidatorFilm()
        film1 = Film(1, "Ion", 999)
        rep = RepoFilme()
        assert rep.size()==0
        rep.store(film1)
        assert rep.size()==1
        film2 = Film(2, "Vasile", 100)
        rep.store(film2)
        assert rep.size()==2
        film3 = Film(2, "Ana", 200)
        try:
            rep.store(film3)
            assert False
        except RepositoryError:
            pass
    def testSearchNume (self):
        film = Film(23, "asd", 100)
        val = ValidatorFilm()
        repo = RepoFilme()
        repo.store(film)
        assert repo.search_nume("asd", 23)==True
    def test_stergeRepoFilme (self):
        film = Film(23, "asd", 100)
        val = ValidatorFilm()
        repo = RepoFilme()
        repo.store(film)
        repo.sterge(23)
        assert repo.size()==0
    def test_sortare_dupa_id(self):
        val = ValidatorFilm()
        repo = RepoFilmeFile("testare/rents_filme.txt")
        srv_filme = ServiceFilme(val, repo)
        srv_filme.sortare_dupa_id()
        assert list(srv_filme.srv_get_film().keys())==[1,2,3]
    def test_delete_film (self):
        val = ValidatorFilm()
        repo = RepoFilme()
        srv_filme = ServiceFilme(val, repo)
        srv_filme.add_film(23, "nume", 100)
        srv_filme.delete_film("nume")
        assert srv_filme.len_filme()==0
    def __test_modifica_film(self):
        val = ValidatorFilm()
        repo = RepoFilme()
        srv_filme = ServiceFilme(val, repo)
        srv_filme.add_film(23, "nume", 100)
        srv_filme.modifica(23, 11, "asd", 123)
        assert repo.get_filme_idx(11).get_nume() == "asd"
        assert repo.get_filme_idx(11).get_pret() == 123
        
    def __creeaza_client_test(self):
        client = Client(1, "Mihai Eminescu", 5211101016382)
        assert (client.get_id_client()==1)
        assert (client.get_nume()=="Mihai Eminescu")
        assert (client.get_cnp()==5211101016382)
    
    def __add_client_test(self):
        validcl = ValidatorClient()
        repocl = RepoClienti()
        srv_cl = ServiceClienti(validcl, repocl)
        try:
            srv_cl.add_client(-1, "nume", 6211101019273)
            assert False
        except ValidationError as ve:
            assert (str(ve)=="id invalid!")
    def __store_client_test(self):
        client = Client(1, "Mihai G", 5211101019273)
        repocl = RepoClienti()
        validarecl = ValidatorClient()
        repocl.store(client)
        assert (repocl.lungime()==1)
        client_bad = Client(-1, "", 2134)
        client_badid = Client(1,"gggg g", 5211101019273)
        try:
            repocl.store(client_badid)
            assert False
        except RepositoryError:
            assert True
            
        assert (repocl.lungime()==1)
    
    
    def __search_client_test(self):
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(23, "nume", 5120308018824)
        srvcl.add_client(55, "Mihai", 5120308018827)
        assert repocl.lungime()==2
        rez = srvcl.srv_search_nume("Mihai")
        assert (rez==[55])
        rez2= srvcl.srv_search_nume("asdsadsadsa")
        assert (rez2 == -1)
    
    
    def __delete_client_test(self):
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(23, "nume", 5120308018824)
        srvcl.add_client(55, "Mihai", 5120308018827)
        srvcl.delete_id_client(55)
        assert repocl.lungime()==1
        try:
            srvcl.delete_id_client(2222)
            assert False 
        except RepositoryError:
            assert True
        assert repocl.lungime()==1
        srvcl.delete_id_client(23)
        assert repocl.lungime()==0
    

    def __modifica_client_test(self):
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(1, "1", 5120308018824)
        srvcl.add_client(2, "2", 5120308018823)
        try:
            srvcl.modifica(2, 3, "3", 5120308018824)
            assert False
        except RepositoryError:
            assert True
        assert repocl.lungime() == 2
    
    
    def __delete_film_id_test(self):
        repofl = RepoFilme()
        validfl = ValidatorFilm()
        srvfl = ServiceFilme(validfl, repofl)
        srvfl.add_film(11, "nume", 150)
        assert repofl.size() == 1
        srvfl.delete_film_by_id(11)
        assert repofl.size()==0
        repofl.store(Film(15, "nume", 150))
        assert repofl.size() == 1
        try:
            repofl.delete_by_id(1000)
            assert False
        except RepositoryError:
            assert True
        try:
            repofl.delete_by_id(15)
        except RepositoryError:
            assert False
        assert repofl.size()==0
        
    
    
    def __creeaza_rent_test(self):
        repor = RepoRent()
        validr = ValidatorRent()
        repoc = RepoClienti()
        repof = RepoFilme()
        servr = ServiceRents(validr, repor, repoc, repof)
        try:    
            servr.creeaza_rent(11, 11, 11)
            assert False
        except ValidationError:
            assert True
    
    
    def __raport_clienti_test(self):
        repofl = RepoFilme()
        validfl = ValidatorFilm()
        srvfl = ServiceFilme(validfl, repofl)
        srvfl.add_film(11, "nume", 150)
        srvfl.add_film(121, "asd", 150)
        srvfl.add_film(12, "asdasd", 150)
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(1, "bircea", 5120308018824)
        srvcl.add_client(2, "alex", 5120308018825)
        repor = RepoRent()
        validr = ValidatorRent()
        servr = ServiceRents(validr, repor, repocl, repofl)
        servr.creeaza_rent(1, 1, 11)
        servr.creeaza_rent(2, 2, 121)
        servr.creeaza_rent(3, 1, 12)
        clienti = servr.get_clienti_sortat()
        assert clienti[0]==["alex", 1]
        assert clienti[1]==["bircea", 2]
        clienti.clear()
        clienti = servr.get_clienti_sortat(True)
        assert clienti[0]==["bircea", 2]
        assert clienti[1]==["alex", 1]
    
    
    def __raport_filme_test(self):
        repofl = RepoFilme()
        validfl = ValidatorFilm()
        srvfl = ServiceFilme(validfl, repofl)
        srvfl.add_film(11, "nume", 150)
        srvfl.add_film(121, "bsd", 150)
        srvfl.add_film(12, "asd", 150)
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(1, "bircea", 5120308018824)
        srvcl.add_client(2, "alex", 5120308018825)
        repor = RepoRent()
        validr = ValidatorRent()
        servr = ServiceRents(validr, repor, repocl, repofl)
        servr.creeaza_rent(1, 1, 11)
        servr.creeaza_rent(2, 2, 121)
        servr.creeaza_rent(3, 1, 12)
        servr.returneaza_film(1)
        servr.creeaza_rent(4, 1, 11)
        filme = servr.get_filme_rents()
        assert filme[0]==("nume", 2)
        assert filme[1]==("bsd", 1)
        assert filme[2]==("asd", 1)
    
    
    def __delete_rent_test(self):
        repofl = RepoFilme()
        validfl = ValidatorFilm()
        srvfl = ServiceFilme(validfl, repofl)
        srvfl.add_film(11, "nume", 150)
        srvfl.add_film(121, "bsd", 150)
        srvfl.add_film(12, "asd", 150)
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(1, "bircea", 5120308018824)
        srvcl.add_client(2, "alex", 5120308018825)
        repor = RepoRent()
        validr = ValidatorRent()
        servr = ServiceRents(validr, repor, repocl, repofl)
        servr.creeaza_rent(1, 1, 11)
        servr.creeaza_rent(2, 2, 121)
        servr.creeaza_rent(3, 1, 12)
        servr.sterge(1)
        assert repor.size()==2
    
    
    def __returneaza_test(self):
        repofl = RepoFilme()
        validfl = ValidatorFilm()
        srvfl = ServiceFilme(validfl, repofl)
        srvfl.add_film(11, "nume", 150)
        repocl = RepoClienti()
        validcl = ValidatorClient()
        srvcl = ServiceClienti(validcl, repocl)
        srvcl.add_client(1, "bircea", 5120308018824)
        repor = RepoRent()
        validr = ValidatorRent()
        servr = ServiceRents(validr, repor, repocl, repofl)
        servr.creeaza_rent(1, 1, 11)
        servr.returneaza_film(1)
        assert repor.get_rent(1).get_status()=="returnat"
    
    
    def run_all_tests(self):
        print ("start teste...")
        self.test_sortare_dupa_id()
        self.testSearchNume()
        self.test_stergeRepoFilme()
        self.test_delete_film()
        self.testStoreFilm()
        self.testValidatorFilm()
        self.__test_modifica_film()
        self.__creeaza_film_test()
        self.__add_film_test()
        self.__delete_film_id_test()
        #------------
        self.__creeaza_client_test()
        self.__add_client_test()
        self.__store_client_test()
        self.__search_client_test()
        self.__delete_client_test()
        self.__modifica_client_test()
        #---
        self.__creeaza_rent_test()
        self.__returneaza_test()
        self.__delete_rent_test()
        self.__raport_clienti_test()
        self.__raport_filme_test()
        
        print ("finish teste...")