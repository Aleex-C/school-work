from infrastructura.repositories import RepoElicopterFile
from business.controller import ServiceElicopter
class Teste():

    def __read_file(self):
        try:
            repo = RepoElicopterFile("test.txt")
            assert len(repo.get_all())==4
        except IOError:
            assert False
    def __cerinta_1(self):
        repo = RepoElicopterFile("test.txt")
        srv_heli = ServiceElicopter(repo)
        rez = srv_heli.cerinta_1("cargo")
        assert len(rez) == 2
        try:
            rez = srv_heli.cerinta_1("scouting")
            assert False
        except Exception:
            assert True
    
    
    def run_all(self):
        self.__read_file()
        self.__cerinta_1()
    
    


