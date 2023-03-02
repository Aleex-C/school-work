from infrastructura.repositories import RepoElicopter, RepoElicopterFile
from business.controller import ServiceElicopter
from interfata.ui import Console
from teste.teste import Teste


if __name__ == '__main__':
    repo = RepoElicopterFile("elicoptere.txt")
    service = ServiceElicopter(repo)
    ui = Console(service)
    teste = Teste()
    
    teste.run_all()
    ui.run()