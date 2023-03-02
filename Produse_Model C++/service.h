#pragma once
#include "repo.h"
#include "validator.h"
class ServiceProduse {
private:
	RepoProduse& repo;
	ProdusValidator val;
public:
	ServiceProduse(RepoProduse& repo, ProdusValidator val) : repo{ repo }, val{ val } {};
	void add(int id, string nume, string tip, double pret) {
		Produs p{ id, nume, tip, pret };
		val.valideaza(p);
		repo.store(p);
	}
	const vector<Produs>& get_all_produse() {
		return repo.get_all();
	}
	int nr_vocale(string nume) {
		int nr = 0;
		for (int i = 0; nume[i]; i++) {
			if (nume[i] == 'a' || nume[i] == 'e' || nume[i] == 'i' || nume[i] == 'o' || nume[i] == 'u') {
				nr++;
			}
		}
		return nr;
	}
	
};