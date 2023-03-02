from prezentare.ui import Console
from business.services import ServiceFilme, ServiceClienti, ServiceRents
from infrastructura.repositories import RepoFilme, RepoClienti, RepoRent
from validare.validators import ValidatorFilm, ValidatorClient, ValidatorRent
from testare.teste import Teste
from infrastructura.file_repositories import RepoFilmeFile, RepoClientiFile,\
    RepoRentsFile

if __name__ == "__main__":
    valid_film = ValidatorFilm()
    valid_client = ValidatorClient()
    valid_rent = ValidatorRent()

    repo_filme = RepoFilmeFile("filme.txt")
    repo_clienti = RepoClientiFile("clienti.txt")
    repo_rents = RepoRentsFile("rents.txt")

    srv_filme = ServiceFilme(valid_film, repo_filme)
    srv_clienti = ServiceClienti(valid_client, repo_clienti)
    srv_rents = ServiceRents(valid_rent, repo_rents, repo_clienti, repo_filme)
    
    ui = Console(srv_filme, srv_clienti, srv_rents)
    

    teste = Teste()
    teste.run_all_tests()
    ui.run()
