class Console(object):
    def __init__(self, srv_elicoptere):
        self.__srv_elicoptere = srv_elicoptere

    
    def __ui_cerinta_1(self):
        scop_cautat = input("Introduceti scopul elicopterelor pe care le cautati: ")
        try:
            rezultat = self.__srv_elicoptere.cerinta_1(scop_cautat)
            for elicopter in rezultat:
                print (elicopter)
        except Exception as ex:
            print (str(ex))
    
    
    def __ui_print(self):
        elicoptere = self.__srv_elicoptere.get_all_helis()
        for heli in elicoptere:
            print (heli)
    
    
    def __ui_cerinta_2(self):
        raspuns = self.__srv_elicoptere.cerinta_2()
        for scop, ani in raspuns.items():
            print (scop, "->", ', '.join(map(str, ani)))
    
    
    def run(self):
        while True:
            cmd = input (">>>")
            if cmd == "exit":
                return
            if cmd == "":
                continue
            elif cmd == "1":
                self.__ui_cerinta_1()
            elif cmd == "2":
                self.__ui_cerinta_2()
            elif cmd == "print":
                self.__ui_print()
            else:
                print("Comanda invalida!")


