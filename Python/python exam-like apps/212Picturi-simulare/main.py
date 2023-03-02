
from validator.validare import ValidatorPictura
from infrastructure.repositories import RepoPicturi, RepoPicturiFile
from business.services import ServicePicturi
from presentation.ui import Console
from teste.teste import Teste

if __name__ == '__main__':
    valid_pictura = ValidatorPictura()
    repo_picturi = RepoPicturiFile("picturi.txt")
    srv_picturi = ServicePicturi(valid_pictura, repo_picturi)
    ui = Console(srv_picturi)
    teste = Teste()
    
    teste.run_all_teste()
    ui.run()