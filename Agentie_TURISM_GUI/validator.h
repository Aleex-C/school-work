#pragma once

#include "oferta.h"
#include <vector>
#include <string>

using std::string;
using std::vector;

class ValidationException {
	vector<string> errorMsg;
public:
	ValidationException(vector<string> msg) : errorMsg{ msg } {};

	string getEM() {
		string err = "";
		for (const string e : errorMsg) {
			err += e + "\n";
		}
		return err;
	}
};
class OfertaValidator {
public:
	void valideaza(const Oferta& o) {
		vector<string> err;
		if (o.getDenumire() == "")
			err.push_back("Denumirea nu poate sa fie vida!");
		if (o.getDestinatie() == "")
			err.push_back("Destinatia nu poate sa fie vida!");
		if (o.getTip() == "")
			err.push_back("Tipul ofertei nu poate fi vid!");
		if (o.getPret() < 0)
			err.push_back("Pretul trebuie sa fie mai mare sau egal cu 0!");
		if (err.size() > 0)
			throw ValidationException(err);
	}
};

void testValidator();