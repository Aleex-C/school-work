from erori.exceptions import ValidationError
class ValidatorFilm(object):
    def validate(self, film):
        err=""
        if film.get_id_film()=="" or film.get_id_film()<0:
            err +="id invalid!"
        elif film.get_nume()=="":
            err +="nume invalid!"
        elif film.get_pret()=="" or film.get_pret()<0:
            err += "pret invalid!"
        if len(err)>0:
            raise ValidationError(err)

class ValidatorClient(object):
    def validate (self, client):
        err=""
        if client.get_id_client()=="" or client.get_id_client()<0:
            err +="id invalid!"
        elif client.get_nume() == "":
            err +="nume invalid"
        elif client.get_cnp()=="" or len(str(client.get_cnp()))!=13:
            err += "cnp invalid!"
        if len(err)>0:
            raise ValidationError(err)
class ValidatorRent (object):
    def validate (self, rent):
        err=""
        if rent.get_id_rent() == "" or rent.get_id_rent()<0:
            err += "id imprumut invalid!"
        elif rent.get_id_client()=="" or rent.get_id_client()<0:
            err +="id client invalid!"
        elif rent.get_id_film()=="" or rent.get_id_film()<0:
            err +="id film invalid!"
        if len(err)>0:
            raise ValidationError(err)