from errors.exceptii import ValidationError


class ValidatorProdus(object):
    def validate (self, produs):
        if produs.get_id_produs()=="" or produs.get_id_produs()<0:
            raise ValidationError("ID invalid!")
        if produs.get_denumire()=="":
            raise ValidationError("Denumire invalida!")
        if produs.get_pret()=="" or produs.get_pret()<0:
            raise ValidationError("Pret invalid!")
        