from presentation.ui import Console
from infrastructure.repositories import RepoSpectacoleFile
from domain.validators import ValidatorSpectacole
from business.services import ServiceSpectacole
if __name__ == '__main__':
    repo_spectacole = RepoSpectacoleFile("spectacole.txt")
    
    valid_spectacole = ValidatorSpectacole()
    
    srv_spectacole = ServiceSpectacole(repo_spectacole, valid_spectacole)
    
    ui = Console(srv_spectacole)
    
    ui.run()
    