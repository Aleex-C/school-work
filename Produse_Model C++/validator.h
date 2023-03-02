#pragma once
#include "produs.h"
#include <vector>
class ValidationError {
	vector<string> errorMsg;
public:
	ValidationError(vector<string> msg) : errorMsg{ msg } {};
	string getMsg() {
		string err = "";
		for (const string eroare : errorMsg) {
			err += eroare + '\n';
		}
		return err;
	}
};

class ProdusValidator {
public:
	void valideaza(const Produs& p) {
		vector<string> err;
		if (p.get_nume() == "") {
			err.push_back("Numele nu poate fi vid!");
		}
		if (p.get_pret() < 1 || p.get_pret() > 100) {
			err.push_back("Pretul trebuie sa fie cuprins intre 1 si 100");
		}
		if (err.size() > 0)
			throw ValidationError(err);
	}
};