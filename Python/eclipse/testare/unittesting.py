import unittest
from validare.validators import ValidatorFilm, ValidatorClient, ValidatorRent
from business.services import ServiceFilme, ServiceClienti, ServiceRents
from infrastructura.file_repositories import RepoFilme, RepoFilmeFile,\
    RepoClientiFile, RepoRentsFile
from erori.exceptions import ValidationError, RepositoryError
import random
from sortare.sortari import MergeSorter, BingoSorter
from domain.entities import Film


class TestCaseFilm(unittest.TestCase):

    def setUp (self):
        val = ValidatorFilm()
        self.srv = ServiceFilme(val, RepoFilmeFile("../test_filme.txt"))
        self.srv.add_film(1, "Godfather", 1200)
    def tearDown(self):
        with open("../test_filme.txt", "w") as f:
            f.write("")
    def testCreate(self):
        self.assertTrue(self.srv.len_filme()==1)
        self.assertRaises(ValidationError, self.srv.add_film, 2, "", 150)
        self.assertRaises(RepositoryError, self.srv.add_film, 1, "nume", 150)
    def testRemove(self):
        self.assertRaises(RepositoryError, self.srv.delete_film_by_id, 2)
        self.assertTrue(self.srv.len_filme()==1)
        film = self.srv.afisare_idx(1)
        self.srv.delete_film_by_id(1)
        self.assertTrue(self.srv.len_filme()==0)
        self.assertEquals(film.get_id_film(), 1)
        self.assertTrue(film.get_nume()=="Godfather")
        self.assertEquals(film.get_pret(), 1200)
    def testFind (self):
        self.assertTrue(self.srv.srv_search_nume("Godfather")==[1])
    def testModify (self):
        self.srv.modifica(1, 10, "Interstellar", 255)
        self.assertTrue(self.srv.afisare_idx(10).get_nume()=="Interstellar")
class TestCaseClient (unittest.TestCase):
    def setUp (self):
        val = ValidatorClient()
        self.srv = ServiceClienti(val, RepoClientiFile("../test_clienti.txt"))
        self.srv.add_client(1, "Alex", 5031209429858)
    def tearDown (self):
        with open("../test_clienti.txt", "w") as f:
            f.write("")
    def testCreate (self):
        self.assertTrue(self.srv.len_clienti()==1)
        self.assertRaises(ValidationError, self.srv.add_client ,2, "", 2405 )
        self.assertRaises(RepositoryError, self.srv.add_client, 1, "mihai", 5031209429858)
    def testRemove (self):
        self.assertRaises(RepositoryError, self.srv.delete_id_client, 2)
        self.assertTrue(self.srv.len_clienti()==1)
        client = self.srv.get_client_dupa_id(1)
        self.srv.delete_id_client(1)
        self.assertTrue(self.srv.len_clienti()==0)
        self.assertEquals(client.get_id_client(),1)
        self.assertTrue(client.get_nume()=="Alex")
        self.assertTrue(client.get_cnp()==5031209429858)
    def testModify (self):
        self.srv.modifica(1, 10, "Mihai", 5031209429858)
        self.assertTrue(self.srv.get_client_dupa_id(10).get_nume()=="Mihai")
class TestCaseRent(unittest.TestCase):
    def setUp(self):
        val = ValidatorRent()
        self.srv = ServiceRents(val, RepoRentsFile("../test_rents.txt"), RepoClientiFile("rents_clienti.txt"), RepoFilmeFile("rents_filme.txt"))
        self.srv.creeaza_rent(1, 1, 1)
    def tearDown(self):
        with open("../test_rents.txt", "w") as f:
            f.write("")
    def testCreate(self):
        self.assertTrue(self.srv.len_rents()==1)
        self.assertRaises(ValidationError, self.srv.creeaza_rent, -12, 2, 2)
        self.assertRaises(RepositoryError, self.srv.creeaza_rent, 1, 2, 2)
    def testRemove (self):
        self.assertRaises (RepositoryError, self.srv.sterge, 2)
        rent = self.srv.get_rent_id(1)
        self.srv.sterge(1)
        self.assertTrue(self.srv.len_rents()==0)
        self.assertEquals(rent.get_id_rent(), 1)
        self.assertTrue (rent.get_id_client()==1)
        self.assertTrue(rent.get_id_film()==1)
    def testModify (self):
        self.srv.returneaza_film(1)
        self.assertTrue(self.srv.get_rent_id(1).get_status()=="returnat")
    def testRapoarte (self):
        self.srv.creeaza_rent(2, 1, 2)
        self.srv.creeaza_rent(3, 2, 3)
        clienti = self.srv.get_clienti_sortat()
        self.assertTrue(clienti[0]==["Alex", 1])
        clienti.clear()
        clienti = self.srv.get_clienti_sortat(True)
        self.assertTrue(clienti[0]==["Mihai", 2])
        self.srv.returneaza_film(1)
        self.srv.creeaza_rent(4, 1, 1)
        filme = self.srv.get_filme_rents()
        self.assertTrue(filme[0]==("Godfather", 2))
class TestCaseSortare(unittest.TestCase):
    def test_all(self):
        sorter = MergeSorter()
        self.__test_sorter(sorter)
        sorter = BingoSorter()
        self.__test_sorter(sorter)

    
    def __simple_int_list_sorter(self, sorter):
        values = [1, 2, 3, 4, 5, 6]
        random.shuffle(values)
        sorter.sort(values)
        assert (values==[1, 2, 3, 4, 5, 6])
        sorter.sort(values, reverse=True)
        assert (values==[6,5,4,3,2,1])
        sorter.sort(values, cmp = lambda x,y: x>=y)
        assert (values==[6,5,4,3,2,1])
    def __str_list_sorter(self, sorter):
        values = ["bro", "alex","aamerica","barca"]
        sorter.sort(values)
        assert (values == ["aamerica", "alex", "barca", "bro"])
        
    def __object_sorter(self, sorter):
        f1 = Film(1,"Godfather",120)
        f2 = Film(2,"LOTR", 150)
        f3 = Film(3,"Morometii", 200)
        values = [f1, f2,f3]
        random.shuffle(values)
        sorter.sort(values, key=lambda x: x.get_nume())
        assert values==[f1, f2, f3]
        f4 = Film (4, "Godfather", 100)
        values.append(f4)
        random.shuffle(values)
        sorter.sort(values, key= lambda x: (x.get_nume(), x.get_pret()))
        assert values == [f4,f1,f2,f3]
        sorter.sort(values, key= lambda x: (x.get_nume(), x.get_pret()), reverse=True)
        assert values == [f3,f2,f1,f4]
        

    def __test_sorter(self, sorter):
        self.__simple_int_list_sorter(sorter)
        self.__str_list_sorter(sorter)
        self.__object_sorter(sorter)
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()