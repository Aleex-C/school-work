#pragma once
#include <string>
#include <assert.h>
#include <iostream>

using std::string;
using std::strcmp;
class OfertaException {
	string msg;
public:
	OfertaException(const string& m) :msg{ m } {};
	string getMsg()const { return msg; }
};
class Oferta {
private:
	string denumire = "";
	string destinatie = "";
	string tip = "";
	int pret = 0;
public:
	const string& getDenumire() const noexcept;
	const string& getDestinatie() const noexcept;
	const string& getTip() const noexcept;
	int getPret() const noexcept;
	void set_dnm(string dnm);
	void set_dest(string dest);
	void set_tip(string tip);
	void set_pret(int pret);

	Oferta(string denumire, string destinatie, string tip, int pret):
		denumire{ denumire }, destinatie{ destinatie }, tip{ tip }, pret{ pret }{
	}
	Oferta() = default;
	//Oferta(const Oferta& ot): denumire{ ot.denumire }, destinatie{ ot.destinatie }, tip{ ot.tip }, pret{ot.pret} {
		//std::cout << "1"<<'\n';
	//}
	
	
};

void test_getters();

bool cmpDenumire(const Oferta& o1, const Oferta& o2)  noexcept;
bool cmpDestinatie(const Oferta& o1, const Oferta& o2)  noexcept;
bool cmpTipPret(const Oferta& o1, const Oferta& o2)  noexcept;