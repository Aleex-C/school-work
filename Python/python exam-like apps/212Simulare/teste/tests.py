from infrastructure.repositories import RepoConcurentiFile, RepoParticipariFile
from business.controller import ServiceConcurenti, ServiceParticipari
class Teste(object):

    
    def __read_concurenti_test(self):
        repo_conc = RepoConcurentiFile("testec.txt")
        assert len(repo_conc.get_all())==3
    
    
    def __read_participari_test(self):
        repo_part = RepoParticipariFile("testep.txt")
        assert len(repo_part.get_all())==3
    
    
    def __cerinta_1_test(self):
        repo_conc = RepoConcurentiFile("testec.txt")
        srv_c = ServiceConcurenti(repo_conc)
        rez = srv_c.cautare_dupa_an(2000)
        assert len(rez)==1
        assert rez[0].get_nume()=="Mihalache"
        

    
    def __cerinta_2_test(self):
        repo_conc = RepoConcurentiFile("testec.txt")
        repo_part = RepoParticipariFile("testep.txt")
        srv_p = ServiceParticipari(repo_part, repo_conc)
        rez = srv_p.clasament()
        assert len(rez)==3
        assert rez[0][0]=="Canada"
        assert rez[1][0]=="Romania"
    
    
    def __get_lista_tari_test(self):
        repo_conc = RepoConcurentiFile("testec.txt")
        repo_part = RepoParticipariFile("testep.txt")
        srv_p = ServiceParticipari(repo_part, repo_conc)
        rez = srv_p.get_list_tari()
        assert len(rez)==3
        assert "Romania" in rez
    
    
    def __get_an_test(self):
        repo_conc = RepoConcurentiFile("testec.txt")
        srv_conc = ServiceConcurenti(repo_conc)
        assert srv_conc.get_an("22.10.2021")==2021
        
    
    
    def run_all(self):
        self.__read_concurenti_test()
        self.__read_participari_test()
        self.__get_an_test()
        self.__cerinta_1_test()
        self.__get_lista_tari_test()
        self.__cerinta_2_test()


