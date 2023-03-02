from errors.exceptii import ValidationError, RepositoryError
class Console(object):
    def __init__(self, srv_produse):
        self.__srv_produse = srv_produse

    
    def __ui_menu(self):
        print ("===MENU===")
        print ("add_produs -> Adauga produs: id (natural pozitiv), denumire, pret (natural pozitiv)")
    
    
    def __ui_add_produs(self):
        try:
            id_produs = int(input("ID produs: "))
        except ValueError:
            print ("ID invalid!")
            return    
        denumire = input("Denumirea produslui: ")
        try:
            pret = int(input("Pret produs: "))
        except ValueError:
            print ("Pret invalid!")
            return 
        try:
            self.__srv_produse.adauga_produs(id_produs, denumire, pret)
            print ("Produs adaugat cu succes!")
        except ValidationError as ve:
            print(ve)
            return
        except RepositoryError as re:
            print(re)
            return
        
    
    
    def __ui_print(self):
        for produs in self.__srv_produse.get_all_produse():
            print(produs)
    
    
    def __ui_delete_digit(self):
        try:
            digit = int(input("Introduceti o cifra [0-9] dupa care doriti sa faceti stergerea: "))
            if digit > 9 or digit < 0:
                print ("Valoare invalida!")
                return
            nr = self.__srv_produse.delete_by_digit(digit)
            print ("Au fost sterse", nr, "produse!")
        except ValueError:
            print ("Valoare invalida!")
    
    
    def __ui_filter(self):
        text = input("Introduceti denumirea produsului pentru filtru (sau -1 pentru off):")
        pret = int(input("Introduceti pret filtru:"))
        rez = self.__srv_produse.filtrare(text, pret)
        for i in rez:
            print(i)
    
    
    def __ui_undo(self):
        print(self.__srv_produse.undo_delete())
    
    
    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "":
                continue
            elif cmd == "exit":
                return
            elif cmd == "menu":
                self.__ui_menu()
            elif cmd == "add_produs":
                self.__ui_add_produs()
            elif cmd == "delete_digit":
                self.__ui_delete_digit()
            elif cmd == "filter":
                self.__ui_filter()
            elif cmd == "undo":
                self.__ui_undo()
            elif cmd == "print":
                self.__ui_print()
            else:
                print("comanda invalida!")
            
            


