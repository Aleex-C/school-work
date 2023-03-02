from erroare.exceptii import ValidationError, RepositoryError
class Console(object):
    def __init__(self, srv_spectacole):
        self.__srv_spectacole = srv_spectacole

    
    def __ui_menu(self):
        print ("===MENU===")
        print (" () add_spectacol ")
        print (" () exit")
        print ("() menu")
    
    
    def __ui_add_spectacol(self):
        titlu = input("Titlul spectacolului: ")
        artist = input("Nume artist: ")
        gen = input("Genul: ")
        try:
            durata = int(input("Durata in secunde: "))
        except ValueError:
            print ("valoare invalida!")
            return
        try:
            self.__srv_spectacole.adauga_spectacol(titlu, artist, gen, durata)
            print ("Spectacol adaugat cu succes!")
        except ValidationError as ve:
            print(ve)
            return
    
    
    def __ui_print(self):
        for spectacol in self.__srv_spectacole.get_all_spectacole():
            print (spectacol)
    
    
    def __ui_modifica(self):
        titlu = input("Titlul spectacolului: ")
        artist = input("Nume artist: ")
        gen = input("Genul: ")
        try:
            durata = int(input("Durata in secunde: "))
        except ValueError:
            print ("valoare invalida!")
            return
        gen_nou = input("Genul nou: ")
        try:
            durata_nou = int(input("Durata noua: "))
        except ValueError:
            print ("valoare invalida!")
            return
        try:
            self.__srv_spectacole.modifica(titlu, artist, gen, durata, gen_nou, durata_nou)
            print ("Spectacol modificat cu succes!")
        except ValidationError as ve:
            print(ve)
            return
        except RepositoryError as re:
            print(re)
            return
    
    
    def __ui_generare(self):
        nr = int(input("Numar de generari: "))
        self.__srv_spectacole.generare_spectacole(nr)
    
    
    def __ui_export(self):
        file_export = input("Numele fisierului de export: ")
        self.__srv_spectacole.export(file_export)
    
    
    def run(self):
        self.__ui_menu()
        while True: 
            cmd = input(">>>")
            if cmd == "":
                continue
            elif cmd == "exit":
                return
            elif cmd == "add_spectacol":
                self.__ui_add_spectacol()
            elif cmd == "menu":
                self.__ui_menu()
            elif cmd == "print":
                self.__ui_print()
            elif cmd == "modifica":
                self.__ui_modifica()
            elif cmd =="generare":
                self.__ui_generare()
            elif cmd == "export":
                self.__ui_export()
            else:
                print("comanda invalida!")


