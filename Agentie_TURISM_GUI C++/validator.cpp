#include "validator.h"

void testValidator(){
	Oferta o_den{ "","A","B", 100 };
	Oferta o_dest{ "A", "", "C", 100 };
	Oferta o_tip{ "A", "B", "", 100 };
	Oferta o_pret{ "A", "B", "C", -1 };
	OfertaValidator val;
	try {
		val.valideaza(o_dest);
		assert(false);
	}
	catch(ValidationException& ve) {
		assert(ve.getEM()=="Destinatia nu poate sa fie vida!\n");
	}
	try {
		val.valideaza(o_den);
		assert(false);
	}
	catch (ValidationException) {
		assert(true);
	}
	try {
		val.valideaza(o_tip);
		assert(false);
	}
	catch (ValidationException) {
		assert(true);
	}
	try {
		val.valideaza(o_pret);
		assert(false);
	}
	catch (ValidationException) {
		assert(true);
	}
}
