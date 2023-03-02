#include "repo.h"
#include <assert.h>
#include <fstream>
#include <sstream>

using std::endl;
using std::ifstream;
using std::ofstream;
using std::stringstream;

void OfertaRepo::store(const Oferta& o) {
		for (const Oferta& offe : oferte) {
			if (o.getDenumire() == offe.getDenumire() &&
				o.getDestinatie() == offe.getDestinatie() &&
				o.getTip() == offe.getTip()) {
				throw RepoException("Oferta deja exista!");
			}
		}
		oferte.push_back(o);
}
void OfertaRepo::remove(int idx_stergere) noexcept {
	oferte.erase(oferte.begin()+idx_stergere);
}
const Oferta& OfertaRepo::find_repo(string denumire){
	/*for (const Oferta& o : this->oferte) {
		if (o.getDenumire() == denumire)
			return o;

	}*/
	vector<Oferta>::iterator it = find_if(oferte.begin(), oferte.end(), [=](const Oferta& o) noexcept {return o.getDenumire() == denumire;});
	if (it != oferte.end()) {
		return *it;
	}
	else {
		throw RepoException("Oferta cu denumirea " + denumire + " nu exista in lista de oferte!");
	}
	
}

void OfertaRepo::modifica(const Oferta& of_v, const Oferta& of_n){
	sterge(of_v);
	store(of_n);
}

void testRepo(){
	OfertaRepo repo_oferte;
	Oferta o{"A", "B", "C", 12 };
	repo_oferte.store(o);
	const auto& oferte = repo_oferte.getAll();
	assert(oferte.size() == 1);
	try
	{
		repo_oferte.store(o);
		assert(false);
	}
	catch (RepoException& exc){
		string msj = exc.getMessage();
		assert(true);
	}
	repo_oferte.remove(0);
	assert(oferte.size() == 0);

	
	
}

void RepoFile::loadFromFile()
{
	ifstream ofertaFile(this->filename);
	if (!ofertaFile.is_open()) {
		throw RepoException("Cannot read from file " + filename);
	}
	string line;
	while (getline(ofertaFile, line))
	{
		string denumire, destinatie, tip;
		int pret;

		stringstream linestream(line);
		string current_item;
		int item_no = 0;
		while (getline(linestream, current_item, ','))
		{
			if (item_no == 0) denumire = current_item;
			if (item_no == 1) destinatie = current_item;
			if (item_no == 2) tip = current_item;
			if (item_no == 3) pret = stoi(current_item);
			item_no++;
		}
		Oferta s{denumire,destinatie,tip,pret};

		OfertaRepo::store(s);


	}
	ofertaFile.close();
}


void RepoFile::saveToFile(){
	ofstream ofertaOutput(this->filename);
	if (!ofertaOutput.is_open())
		throw RepoException("Cannot write to file " + filename);
	for (auto& oferta : getAll()) {
		ofertaOutput << oferta.getDenumire() << "," << oferta.getDestinatie() << ",";
		ofertaOutput << oferta.getTip() << "," << oferta.getPret() << endl;
	}
	ofertaOutput.close();
}

void RepoFile::store(const Oferta& s){
	OfertaRepo::store(s);

	saveToFile();
}

void RepoFile::remove(int idx_stergere) noexcept
{
	OfertaRepo::remove(idx_stergere);
	saveToFile();
}

void RepoFile::sterge(const Oferta& p){
	OfertaRepo::sterge(p);
	saveToFile();
}
