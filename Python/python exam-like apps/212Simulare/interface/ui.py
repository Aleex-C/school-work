class Console(object):
    def __init__(self, srv_c, srv_p):
        self.__srv_c = srv_c
        self.__srv_p = srv_p

    
    def __ui_cerinta_1(self):
        '''Afiseaza rezolvarea primei cerinte: Concurenti cautati dupa anul de nastere'''
        try:
            an_cautat = int(input("Introduceti anul nasterii de la care sa inceapa cautarea: "))
            if (len(str(an_cautat))!=4):
                print ("Anul introdus este gresit!")
                return
        except ValueError:
            print("Valoare numerica invalida!")
            return
        try:
            solutie = self.__srv_c.cautare_dupa_an(an_cautat)
            for concurent in solutie:
                print (concurent)
        except Exception as ex:
            print(str(ex))
    
    
    def __ui_cerinta_2(self):
        '''Afiseaza rezlvarea cerintei 2: Clasamentul pe tari, sortat dupa punctaj'''
        print ("CLASAMENT")
        print ("==========")
        raspuns = self.__srv_p.clasament()
        for t,p in raspuns:
            print(t, "->", p)
    
    
    def run(self):
        print("MENU")
        print("===========")
        print("1 -> Cauta concurentii nascuti dupa un an dat")
        print("2 -> Afiseaza clasamentul pe tari")
        while True:
            cmd = input (">>>")
            if cmd == "exit":
                return
            elif cmd == "":
                continue
            elif cmd == "1":
                self.__ui_cerinta_1()
            elif cmd == "2":
                self.__ui_cerinta_2()
            else:
                print ("Comanda invalida!")
        


