from erori.exceptions import ValidationError
class Film (object):
    def __init__(self, id_film, nume, pret):
        self.__id_film = id_film
        self.__nume = nume
        self.__pret = pret
    def get_id_film(self):
        return self.__id_film
    def get_nume(self):
        return self.__nume
    def get_pret(self):
        return self.__pret
    def set_nume(self, nume):
        self.__nume = nume
    def set_id(self, id_film):
        self.__id_film = id_film
    def set_pret(self, pret):
        self.__pret = pret
    def __repr__(self):
        return "[%s] Film: %s || pret: %s" % (self.__id_film, self.__nume, self.__pret)
    def __str__(self):
        return "[%s] Film: %s || pret: %s" % (self.__id_film, self.__nume, self.__pret)
class Client(object):
    def __init__(self, id_client, nume, cnp):
        self.__id_client = id_client
        self.__nume = nume
        self.__cnp = cnp

    def get_id_client(self):
        return self.__id_client


    def get_nume(self):
        return self.__nume


    def get_cnp(self):
        return self.__cnp


    def set_id_client(self, value):
        self.__id_client = value


    def set_nume(self, value):
        self.__nume = value


    def set_cnp(self, value):
        self.__cnp = value
        
    def __str__(self):
        return "{%s} Nume: %s // CNP: %s" % (self.__id_client, self.__nume, self.__cnp)
class Rent(object):
    def __init__(self, id_rent, id_client, id_film):
        self.__id_rent = id_rent
        self.__id_client = id_client
        self.__id_film = id_film
        self.__status = "imprumutat"

    def get_id_rent(self):
        return self.__id_rent


    def get_id_client(self):
        return self.__id_client


    def get_id_film(self):
        return self.__id_film


    def get_status(self):
        return self.__status
    
    def returnare (self):
        if self.get_status() == "returnat":
            raise ValidationError("Acest client a returnat deja filmul!")
            return 
        self.__status = "returnat"
    
    def __eq__(self, rent):
        return self.get_id_rent() == rent.get_id_rent()
    def __str__(self):
        return "<%s> Id_client: %s | Id_film: %s | Status: %s" % (self.__id_rent, self.__id_client, self.__id_film, self.__status)
        
    