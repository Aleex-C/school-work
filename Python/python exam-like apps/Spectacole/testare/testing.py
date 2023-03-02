'''
Created on 28 Jan 2022

@author: alexx
'''
import unittest
from infrastructure.repositories import RepoSpectacole, RepoSpectacoleFile
from domain.entities import Spectacol
from domain.validators import ValidatorSpectacole
from erroare.exceptii import ValidationError, RepositoryError
from business.services import ServiceSpectacole

class TestService(unittest.TestCase):
    def setUp(self):
        repo = RepoSpectacole()
        valid = ValidatorSpectacole()
        self.srv_spec = ServiceSpectacole(repo, valid)
        
class TestValidare(unittest.TestCase):
    def setUp(self):
        self.__valid = ValidatorSpectacole()
    def testValidate(self):
        spectacol1=Spectacol("","s", "altele", 2)
        spectacol2=Spectacol("s", "", "altele", 2)
        spectacol3=Spectacol("s", "s", "drama", 2)
        spectacol4=Spectacol("s", "s", "comedie", -2)
        self.assertRaises(ValidationError, self.__valid.validate, spectacol1)
        self.assertRaises(ValidationError, self.__valid.validate, spectacol2)
        self.assertRaises(ValidationError, self.__valid.validate, spectacol3)
        self.assertRaises(ValidationError, self.__valid.validate, spectacol4)
class TestRepoSpectacole(unittest.TestCase):
    def setUp(self):
        self.__repo_spectacole = RepoSpectacole()
        self.__repo_spectacole.store(Spectacol("macbeth", "hopkins", "altele", 10))

    def tearDown(self):
        self.__repo_spectacole._spectacole.clear()


    def testStore(self):
        self.assertTrue(self.__repo_spectacole.size()==1)

class TestRepoSpectacoleFile(unittest.TestCase):
    def setUp(self):
        self.__repo = RepoSpectacoleFile("test_spectacole.txt")
        spectacol = Spectacol("macbeth", "hopkins", "altele", 10)
        self.__repo.store(spectacol)
    def tearDown(self):
        with open("test_spectacole.txt", "wt") as f:
            f.write('')
    def testStore(self):
        self.__repo.store(Spectacol("bla", "bla", "comedie", 100))
        self.__repo.store(Spectacol("bla", "bla", "comedie", 101))
        self.assertTrue(self.__repo.size()==3)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()