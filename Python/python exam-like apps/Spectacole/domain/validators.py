from erroare.exceptii import ValidationError
class ValidatorSpectacole(object):
    def validate (self, spectacol):
        err = ""
        if spectacol.get_titlu()=="":
            err+="Titlu vid!\n"
        if spectacol.get_artist()=="":
            err+="Artist vid!\n"
        if spectacol.get_gen() not in ["comedie", "concert", "balet", "altele"]:
            err+="Genul nu este recunoscut!\n"
        if spectacol.get_durata()<0:
            err+="Durata este intreg pozitiv!\n"
        if len(err)>0:
            raise ValidationError(err)

