from infrastructure.repositories import RepoConcurentiFile, RepoParticipariFile
from business.controller import ServiceConcurenti, ServiceParticipari
from interface.ui import Console
from teste.tests import Teste

if __name__ == '__main__':
    repo_concurenti = RepoConcurentiFile("concurenti.txt")
    repo_participari = RepoParticipariFile("participari.txt")
    
    srv_concurent = ServiceConcurenti(repo_concurenti)
    srv_participari = ServiceParticipari(repo_participari, repo_concurenti)
    
    ui = Console(srv_concurent, srv_participari)
    teste = Teste()
    
    teste.run_all()
    ui.run()