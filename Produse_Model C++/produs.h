#pragma once
#include <string>
#include <assert.h>
using namespace std;
class Produs {
private:
	int id;
	string nume;
	string tip;
	double pret;
public:
	Produs(int id, string nume, string tip, double pret) : id{ id }, nume{ nume }, tip{ tip }, pret{ pret }{};
	int get_id() const {
		return this->id;
	}
	string get_nume() const {
		return this->nume;
	}
	string get_tip() const {
		return this->tip;
	}
	double get_pret() const {
		return this->pret;
	}
};