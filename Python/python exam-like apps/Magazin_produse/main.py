
from infrastrucuture.repositories import RepoProduse, RepoProduseFile
from business.services import ServiceProduse
from interface.user_input import Console
from entities.validator import ValidatorProdus

if __name__ == '__main__':
    repo_produse = RepoProduseFile("produse.txt")
    val_produse = ValidatorProdus()
    srv_produse = ServiceProduse(repo_produse, val_produse)
    
    ui = Console(srv_produse)
    
    ui.run()
    