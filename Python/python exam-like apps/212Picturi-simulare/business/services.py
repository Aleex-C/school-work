from domain.entities import Pictura


class ServicePicturi(object):
    def __init__ (self, vp, rp):
        self.__vp = vp #validator_pic
        self.__rp = rp #repo_pic
    def cauta_subtring(self, substring):
        picturi = self.__rp.get_all_pics()
        rez = []
        for pictura in picturi:
            if substring in pictura.get_pic_name():
                rez.append(pictura)
        if len(rez)==0:
            raise Exception("Nu exista niciun tablou care sa contina", substring, "in nume!")
        sortat = sorted(rez, key=lambda x: x.get_year(), reverse=True)
        return sortat
    def picturi_noi(self):
        picturi = self.__rp.get_all_pics()
        sortat = sorted(picturi, key=lambda x: x.get_year(), reverse=True)
        autori = ""
        for pictura in sortat:
            if pictura.get_author_name() not in autori:
                print(f'{pictura.get_author_name()}: {pictura.get_year()}')
                autori += pictura.get_author_name()
    
    



