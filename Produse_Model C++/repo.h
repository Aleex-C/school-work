#pragma once
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include "produs.h"
class RepoException {
	string msg;
public:
	RepoException(string msj) : msg{ msj } {

	}
	string getMessage() {
		return msg;
	}
};
class RepoProduse {
private:
	vector<Produs> produse;
	string path;
public:
	RepoProduse(string file_path) : path{ file_path } {
		load_from_file();
	}
	void store(Produs p) {
		if (find_if(produse.begin(), produse.end(), [=](Produs& p2) {
			return p.get_id() == p2.get_id();
			}) == produse.end()) {
			produse.push_back(p);
			write_to_file();
		}
		else 
			throw(RepoException("Exista deja un produs cu ID identic!"));
		
		
	}
	void write_to_file() {
		ofstream produsOutput(this->path);
		if (!produsOutput.is_open())
			throw RepoException("Cannot write to file " + path);
		for (auto& produs : get_all()) {
			produsOutput << produs.get_id() << "," << produs.get_nume() << ",";
			produsOutput << produs.get_tip() << "," << produs.get_pret() << endl;
		}
		produsOutput.close();
	}
	void load_from_file() {
		ifstream produseFile(this->path);
		if (!produseFile.is_open()) {
			throw RepoException("Cannot open file!");
		}
		string line;
		while (getline(produseFile, line)) {
			int id;
			string nume, tip;
			double pret;
			stringstream flux_linie(line);
			string current;
			vector<string> parts;
			//int no_item = 0;
			while (getline(flux_linie, current, ',')) {
				parts.push_back(current);
			}
			id = stoi(parts[0]);
			nume = parts[1];
			tip = parts[2];
			pret = stod(parts[3]);
			Produs p{ id, nume, tip, pret };
			store(p);
		}
		produseFile.close();
	}
	const vector<Produs>& get_all() {
		sort(produse.begin(), produse.end(), [&](Produs p1, Produs p2) {
			return p1.get_pret() < p2.get_pret();
			});
		return this->produse;
	}
};

void test_file();