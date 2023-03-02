from erori.exceptions import ValidationError, RepositoryError
from random import randrange, choice
from string import ascii_letters

class Console(object):
    def __init__(self, srv_filme, srv_clienti, srv_rents):
        self.__srv_filme = srv_filme
        self.__srv_clienti = srv_clienti
        self.__srv_rents= srv_rents
    
    def __ui_adauga_film(self):
        try:
            id_film = int(input("Id-ul filmului: "))
            if (id_film < 0):
                print ("valoare numerica invalida!")
                return
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        nume = input("Nume film: ")
        try:
            pret = int(input("Pret film: "))
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        try:
            if self.__srv_filme.add_film(id_film, nume, pret)!=-1:
                print ("Film adaugat cu succes!")
        except RepositoryError as re:
            print(re)
        except ValidationError as ve:
            print (str(ve))
            return
    
    def __ui_delete_film(self):
        nume = input("Numele filmului pe care doriti sa-l stergeti din lista: ")
        if self.__srv_filme.delete_film(nume)!=-1:
            print ("Stergerea a avut loc cu succes!")
        else:
            print("Filmul nu exista in lista!")
            
    def __ui_delete_film_id(self):
        id_stergere= int(input("Id-ul filmului pe care doriti sa-l stergeti din lista: "))
        try:
            self.__srv_filme.delete_film_by_id(id_stergere)
            print ("Stergerea a avut loc cu succes!")
        except RepositoryError as re:
            print (str(re))
    def __ui_print_filme(self):
        for film in self.__srv_filme.srv_get_film().values():
            print(film)
    
    def __ui_search_nume_film(self):
        nume = input ("Introduceti numele filmului pe care il cautati: ")
        l = self.__srv_filme.srv_search_nume(nume)
        if l != -1:
            for i in l:
                print(self.__srv_filme.afisare_idx(i))
        else:
            print ("Acest film nu exista!")
    
    def __ui_sort(self):
        self.__srv_filme.sortare_dupa_id()
        self.__ui_print_filme()
    

    def __ui_modifica_film(self):
        print("Introduceti id-ul filmului pe care doriti sa-l modificati:")
        try:
            id_film = int(input())
            if (id_film < 0):
                print ("valoare numerica invalida!")
                return
            if id_film not in self.__srv_filme.srv_get_film():
                print("Nu exista film cu acest id!")
                return
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        print ("Datele curente ale filmului: ", end=' ')
        print(self.__srv_filme.afisare_idx(id_film))
        try:
            id_film_nou = int(input("Id nou: "))
            if (id_film_nou < 0):
                print ("valoare numerica invalida!")
                return
            if id_film_nou != id_film:
                if id_film_nou in self.__srv_filme.srv_get_film():
                    print("Un film cu acest id exista deja!")
                    return
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        nume_nou = input("Nume film: ")
        try:
            pret_nou = int(input("Pret film: "))
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        
        if self.__srv_filme.modifica(id_film, id_film_nou, nume_nou, pret_nou)!=-1:
            print ("Modificat cu succes!")
            self.__ui_print_filme()
    
    
    def __ui_adauga_client(self):
        try:
            id_client = int(input("Introduceti ID client: "))
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        nume = input("Introduceti numele clientului: ")
        try:
            cnp = int(input("Introduceti CNP-ul clientului: "))
            if len(str(cnp))!=13:
                print ("Cnp invalid!")
                return
        except ValueError:
            print ("CNP invalid!")
            return

        try:
            self.__srv_clienti.add_client(id_client, nume, cnp)
            print("Client adaugat cu succes!")
        except ValidationError as ve:
            print (str(ve))
            return
        except RepositoryError as re:
            print (str(re))

    
    def __ui_print_clienti(self):
        clienti = self.__srv_clienti.get_all_clienti()
        if len(clienti)==0:
            print ("Nu exista niciun client in lista!")
        for client in clienti:
            print (client)
            
    
    
    def __ui_delete_client(self):
        try:
            id_client_stergere = int(input("Introduceti ID-ul clientului pe care doriti sa-l stergeti: "))
            if (id_client_stergere<0):
                print ("Valoare numerica invalida!")
                return
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        
        try:
            self.__srv_clienti.delete_id_client(id_client_stergere)
            print ("Stergerea a avut loc cu succes!")
        except RepositoryError:
            print ("Id-ul nu exista!")
    

    def __ui_search_nume_client(self):
        nume_cautat = input("Introduceti numele persoanelor cautate: ")
        rez = self.__srv_clienti.srv_search_nume(nume_cautat)
        if rez == -1:
            print ("Nu exista numele cautat!")
            return
        else:
            clienti = self.__srv_clienti.get_all_clienti()
            for client in clienti:
                for id_client in rez:
                    if client.get_id_client()==id_client:
                        print (client)
        
    
    def __ui_modifica_client(self):
        self.__ui_print_clienti()
        try:
            original = int(input("Introduceti id-ul clientului pe care doriti sa-l modificati: "))
            if (original < 0):
                print ("Valoare numerica invalida!")
                return
            if not any(x.get_id_client() == original for x in self.__srv_clienti.get_clienti()):
                print ("Id-ul nu exsita!")
                return
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        print ("Datele curente ale clientului sunt: ", end=' ')
        print(self.__srv_clienti.get_client_dupa_id(original))
        try:
            id_client_nou = int(input("Introduceti id-ul nou al clientului: "))
            if (id_client_nou < 0):
                print ("Valoare numerica invalida!")
                return
        except ValueError:
            print ("Valoare numerica invalida!")
            return
        nume_nou = input("Introduceti numele nou al clientului: ")
        try:
            CNP_nou = int(input("Introduceti cnp-ul nou al clientului: "))
            if (CNP_nou < 0):
                print ("CNP invalid!")
                return
        except ValueError:
            print ("CNP invalid!")
            return
        try:
            self.__srv_clienti.modifica(original, id_client_nou, nume_nou, CNP_nou)
            print("modificat cu succes!")
        except ValidationError as ve:
            print (str(ve))
            return
        except RepositoryError as re:
            print (str(re))
            return
    
    
    def __ui_rand(self):
        x = int(input("Nr de generari rand: "))
        for i in range(x):
            id_client = randrange(1, 500)
            nume_client = ''.join( choice(ascii_letters) for j in range(0,10))
            CNP_client = randrange(5000000000000, 6000000000000)
            try:
                self.__srv_clienti.add_client(id_client, nume_client, CNP_client)
                print("Client adaugat cu succes!")
            except ValidationError as ve:
                print (str(ve))
                return
            except RepositoryError as re:
                print (str(re))
                return
            
    
    
    def __ui_adauga_rent(self):
        try:
            idr = int(input("Introduceti id-ul inchirierii:"))
            idf = int(input("Introduceti id-ul filmului:"))
            idc = int(input("Introduceti id-ul clientului: "))
        except ValueError:
            print ("Valoare numerica invalida!")
            return 
        try:
            self.__srv_rents.creeaza_rent(idr, idc, idf)
            print("Inchiriere adaugata cu succes!")
        except ValidationError as ve:
            print (str(ve))
            return
        except RepositoryError as re:
            print (str(re))
            return
    
    
    def __ui__delete_rent(self):
        try:
            id_rent_stergere = int(input("Introduceti id-ul inchirierii pe care doriti sa o stergeti: "))
        except ValueError:
            print("Id invalid!")
        try:
            self.__srv_rents.sterge(id_rent_stergere)
            print("Stergerea a avut loc cu succes!")
        except RepositoryError as re:
            print (re)
    
    
    def __ui_print_rents(self, idx=0):
        
        '''rents = self.__srv_rents.get_all_rents()
        if len(rents)!=0:
            for rent in rents:
                print(rent)
        else:
            print("Nu exista niciun imprumut!")'''
        
        rents = self.__srv_rents.get_all_rents()
        #recursiv
        if len(rents)==0:
            print("Nu exista niciun imprumut!")
        else:
            if idx<len(rents):
                print(rents[idx])
                self.__ui_print_rents(idx=idx+1)
    
    
    
    def __ui_return_rent(self):
        try:
            id_rent = int(input("Introduceti id-ul inchirierii cautate: "))
            self.__srv_rents.returneaza_film(id_rent)
        except ValueError:
            print ("ID invalid!")
        except ValidationError as ve:
            print(ve)
        except RepositoryError as re:
            print (re)
        
    
    
    def __ui_raport_clienti_nume(self):
        try:
            clienti = self.__srv_rents.get_clienti_sortat()
            for client in clienti:
                print (client[0] + " -> " + str(client[1]))
        except ValidationError as ve:
            print(ve)
        except RepositoryError as re:
            print (re)
    def __ui_raport_clienti_rents(self):
        try:
            clienti = self.__srv_rents.get_clienti_sortat(ok=True)
            for client in clienti:
                print (client[0] + " -> " + str(client[1]))
        except ValidationError as ve:
            print(ve)
        except RepositoryError as re:
            print (re)
    
    
    def __ui_raport_filme(self):
        filme = self.__srv_rents.get_filme_rents()
        for f in filme:
            print (f[0] + " -> " + str(f[1]))
            
    def __ui_raport_filme_top_3(self):
        filme = self.__srv_rents.get_filme_rents()
        for f in filme[:3]:
            print (f[0] + " -> " + str(f[1]))
    
    def __ui_raport_clienti_30(self):
        try:
            clienti = self.__srv_rents.get_clienti_sortat(ok=True)
            for client in clienti[:int(1+len(clienti)*0.3)]:
                print (client[0] + " -> " + str(client[1]))
        except ValidationError as ve:
            print(ve)
        except RepositoryError as re:
            print (re)
    
    
    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "":
                continue
            elif cmd == "exit":
                return
            elif cmd == "add_film":
                self.__ui_adauga_film()
            elif cmd == "add_client":
                self.__ui_adauga_client()
            elif cmd == "add_rent":
                self.__ui_adauga_rent()
            elif cmd == "delete_film":
                self.__ui_delete_film()
            elif cmd == "delete_film_id":
                self.__ui_delete_film_id()
            elif cmd == "delete_client":
                self.__ui_delete_client()
            elif cmd == "delete_rent":
                self.__ui__delete_rent() 
            elif cmd == "print_filme":
                self.__ui_print_filme()
            elif cmd == "print_clienti":
                self.__ui_print_clienti()
            elif cmd == "print_rents":
                self.__ui_print_rents()
            elif cmd == "search_nume_film":
                self.__ui_search_nume_film()
            elif cmd == "search_nume_client":
                self.__ui_search_nume_client()
            elif cmd == "sort":
                self.__ui_sort()
            elif cmd == "mod_film":
                self.__ui_modifica_film()
            elif cmd == "mod_client":
                self.__ui_modifica_client()
            elif cmd == "returneaza":
                self.__ui_return_rent()
            elif cmd == "raport_clienti_nume":
                self.__ui_raport_clienti_nume()
            elif cmd == "raport_clienti_rents":
                self.__ui_raport_clienti_rents()
            elif cmd == "raport_filme":
                self.__ui_raport_filme()
            elif cmd == "raport_filme_top_3":
                self.__ui_raport_filme_top_3()
            elif cmd == "raport_clienti_30":
                self.__ui_raport_clienti_30()
            elif cmd == "rand":
                self.__ui_rand()
            else:
                print ("comanda invalida!")