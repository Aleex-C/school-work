class ServiceConcurenti(object):
    def __init__(self, repo_c):
        self.__repo_c = repo_c
    def get_an(self, data_nasterii):
        '''Returneaza anul cautat din formatul dd.mm.yyyy'''
        parts = data_nasterii.split('.')
        return int(parts[2])
        
    def cautare_dupa_an (self, an_cautat):
        '''Cauta concurentii care au ca an al nasterii o valoare mai mare decat anul_cautat
            returneaza lista cu astfel de concurenti
        '''
        concurenti = self.__repo_c.get_all()
        rez = []
        for concurent in concurenti:
            if an_cautat < self.get_an(concurent.get_data_nasterii()):
                rez.append(concurent)
        if len(rez)==0:
            raise Exception("Nu exista concurenti nascuti dupa acest an!")
        return rez 
    


class ServiceParticipari(object):
    def __init__(self, repo_p, repo_c):
        self.__repo_p = repo_p
        self.__repo_c = repo_c
    def get_list_tari(self):
        '''Functia returneaza lista cu toate tarile care au participat la concursul sportiv'''
        participari = self.__repo_p.get_all()
        tari = ""
        rez = []
        for participare in participari:
            tara = self.__repo_c.get_by_id(participare.get_id_c()).get_tara()
            if tara not in tari:
                rez.append(tara)
                tari += tara
        return rez
    def clasament (self):
        '''Functia returneaza o lista sortata de tupluri in care 'key' este tara, iar 'value' este
            punctajul total obtinut de toti participantii tarii respective
             sortarea este descrescatoare, in functie de punctaj
        '''
        tari = self.get_list_tari()
        participari = self.__repo_p.get_all()
        rez = {}
        for tara in tari:
            rez[tara] = 0
            for participare in participari:
                if self.__repo_c.get_by_id(participare.get_id_c()).get_tara() in tara:
                    rez[tara] = rez[tara] + int(participare.get_punctaj())
                    
        sortat = sorted(rez.items(), key=lambda x: x[1], reverse=True)
        return sortat
            


