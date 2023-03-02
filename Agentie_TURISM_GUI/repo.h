#pragma once
#include <vector>
#include "oferta.h"
//#include "VectDin.h"
using std::vector;

class RepoException {
	string msg;
public:
	RepoException(string msj) : msg{ msj } {

	}
	string getMessage() {
		return msg;
	}
};
class OfertaRepo {
private:
	vector<Oferta> oferte;
public:
	OfertaRepo(const OfertaRepo& ot) = delete;
	OfertaRepo() noexcept = default;
	virtual void store(const Oferta& o);
	virtual void remove(int idx_stergere) noexcept;
	const vector<Oferta>& getAll() noexcept {
		return oferte;
	}
	/*vector<Oferta>& getAll2() {
		return oferte;
	}*/
	const Oferta& find_repo(string denumire);
	void modifica(const Oferta& of_v, const Oferta& of_n);
	virtual void sterge(const Oferta& p) {
		auto found = std::find_if(oferte.begin(), oferte.end(), [p](const Oferta& pp) noexcept {
			return pp.getDenumire() == p.getDenumire();
			});
		if (found == oferte.end()) {
			throw OfertaException{ "Oferta inexistenta!" };
		}
		//stergem pet
		auto rez = oferte.erase(found);
	}
};

class RepoFile : public OfertaRepo {
private:
	string filename;
	/*
	Incarca datele din fisier
	*/
	void loadFromFile();
	/*
	* Salveaza datele din fisier
	* Format: titlu,artist,gen,durata\n
	*/
	void saveToFile();
public:
	RepoFile(string fname) :OfertaRepo(), filename{ fname } {
		loadFromFile();
	};
	void store(const Oferta& s) override;
	void remove(int idx_stergere) noexcept override;
	void sterge(const Oferta& p) override;
 };

void testRepo();