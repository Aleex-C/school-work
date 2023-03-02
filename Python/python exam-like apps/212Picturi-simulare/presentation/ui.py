class Console(object):
    
    
    def __init__(self, srv_picturi):
        self.__srv_picturi = srv_picturi

    
    def __ui_afisare_substring(self):
        substr = input("Introduceti substringul cautat: ")
        try:
            rez = self.__srv_picturi.cauta_subtring(substr)
            for pic in rez:
                print (pic)
        except Exception as ex:
            print (str(ex))
    
    
    def __ui_afisare_2(self):
        self.__srv_picturi.picturi_noi()
    
    
    def run(self):
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return 
            if cmd == "":
                continue
            elif cmd == "1":
                self.__ui_afisare_substring()
            elif cmd == "2":
                self.__ui_afisare_2()
            else:
                print("Comanda invalida!")  
    
    



