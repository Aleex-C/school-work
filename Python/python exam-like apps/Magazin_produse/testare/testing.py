import unittest
from infrastrucuture.repositories import RepoProduse, RepoProduseFile
from entities.produs import Produs
from errors.exceptii import RepositoryError, ValidationError
from entities.validator import ValidatorProdus
from business.services import ServiceProduse

class TestServiceProduse(unittest.TestCase):
    def setUp(self):
        repo_produse = RepoProduse()
        val_produse = ValidatorProdus()
        self.srv_produse = ServiceProduse(repo_produse, val_produse)
    def testServiceAdaugaProdus(self):
        self.srv_produse.adauga_produs(1, "lapte", 5)
        self.assertTrue(len(self.srv_produse.get_all_produse())==1)
        self.assertRaises(ValidationError, self.srv_produse.adauga_produs, 2, "l",-1)
        self.assertRaises(ValidationError, self.srv_produse.adauga_produs, -1, "l",1)
        self.assertRaises(ValidationError, self.srv_produse.adauga_produs, "", "",1)
        self.assertRaises(ValidationError, self.srv_produse.adauga_produs, 1, "",1)
    def testDeleteDigit(self):
        self.srv_produse.adauga_produs(1, "lapte", 5)
        self.srv_produse.delete_by_digit(5)
        self.assertTrue(len(self.srv_produse.get_all_produse())==0)
    def testFilter(self):
        self.srv_produse.adauga_produs(1, "lapte", 5)
        self.assertTrue(self.srv_produse.filtrare("lapte", -1)[0].get_id_produs()==1)
    def testUndo(self):
        self.srv_produse.adauga_produs(1, "lapte", 5)
        self.srv_produse.delete_by_digit(5)
        self.assertTrue(self.srv_produse.undo_delete()=="Successful undo!")   
class TestRepoProduse(unittest.TestCase):


    def setUp(self):
        self.repo = RepoProduse()
        produs = Produs(1, "Paine", 5)
        self.repo.store(produs)

    def tearDown(self):
        self.repo._produse.clear()
    def testStore(self):
        self.assertTrue(self.repo.size()==1)
        self.assertRaises(RepositoryError, self.repo.store, Produs(1, "Lapte", 5))
    def testDelete(self):
        self.repo.delete(1)
        self.assertTrue(self.repo.size()==0)
        self.assertRaises(RepositoryError, self.repo.delete, 1)

class TestRepoFileProduse (unittest.TestCase):
    def setUp(self):
        self.repo = RepoProduseFile("test_produse.txt")
        self.repo.store(Produs(1, "lapte", 10))
    def tearDown(self):
        with open("test_produse.txt", "wt") as f:
            f.write("")
    def testFileStore(self):
        self.assertTrue(self.repo.size()==1)
if __name__ == "__main__":
    unittest.main()