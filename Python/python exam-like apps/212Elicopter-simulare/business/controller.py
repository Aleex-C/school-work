class ServiceElicopter(object):
    def __init__(self, repo):
        self.__repo = repo
    def cerinta_1(self, scop_cautat):
        elicoptere = self.__repo.get_all()
        rez = []
        for elicopter in elicoptere:
            if elicopter.get_scop() in scop_cautat:
                rez.append(elicopter)
        if len(rez)==0:
            raise Exception("Nu exista elicoptere care sa indeplineasca acest scop!")
        
        sortat = sorted(rez, key=lambda x: x.get_name(), reverse=True)
        return sortat
    def cerinta_2(self):
        scopuri = self.get_scopuri()
        helis = self.__repo.get_all()
        rez = {}
        for scop in scopuri:
            rez_ani = []
            for heli in helis:
                if heli.get_scop()==scop:
                    rez_ani.append(heli.get_year())
            rez[scop]=rez_ani
        return rez
            
                    
                        
    def get_all_helis(self):
        return self.__repo.get_all()
    def get_scopuri (self):
        helis = self.__repo.get_all()
        scopuri = ""
        rez = []
        for heli in helis:
            if heli.get_scop() not in scopuri:
                rez.append(heli.get_scop())
                scopuri += heli.get_scop()
        return rez
        


