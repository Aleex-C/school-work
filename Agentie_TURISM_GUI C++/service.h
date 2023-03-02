#pragma once
#include <string>
#include "oferta.h"
#include "export.h"
#include "repo.h"
#include "validator.h"
#include "Wishlist.h"
#include "undo.h"
#include <functional>
#include <algorithm>
#include <map>
using std::string;
using std::map;
using std::pair;
using std::unique_ptr;
using std::vector;

class OferteService {
private:
	OfertaRepo& repo;
	OfertaValidator& val;
	Wishlist wish;
	vector<unique_ptr<ActiuneUndo>> undoList;
public:
	OferteService(OfertaRepo& repo, OfertaValidator& val) noexcept : repo{ repo }, val{ val } {};
	OferteService(const OferteService& ot) = delete;
	OferteService() = default;
	int add(string denumire, string destinatie, string tip, int pret);
	int dlt(string dnm, string dest, string tp, int pret);
	int modify(string dnm, string dest, string tp, int pret, string dnm_n, string dest_n, string tp_n, int pret_n);
	const vector<Oferta>& getAll() noexcept {
		return repo.getAll();
	}
	/*vector<Oferta>& getAll2() {
		return repo.getAll2();
	}*/
	const vector<Oferta>& getWishlistOferte() noexcept;
	const Oferta& find(string denumire) const;
	vector<Oferta> filter(std::function<bool(const Oferta&)> fct);
	vector<Oferta> dest_filter(string dest);
	vector<Oferta> pret_filter(int pret);
	vector<Oferta> sortedDenumire();
	vector<Oferta> sortedDestinatie();
	vector<Oferta> sortedTipPret();
	vector<Oferta> generalSort(bool(*maiMicF)(const Oferta&, const Oferta&));
	void addToWishlist(string denumire);
	const size_t addRandomToWishlist(int cate);
	void emptyWishlist() noexcept;
	map<const int, size_t> rapoarte_Pret();
	void exportaCosCVS(string fName) const;
	void undo();
	Wishlist& getWishlist2() {
		return this->wish;
	}
};

void testAdd();
void testRemove();
void testModify();
void testFind();
void testFilter();
void testSort();
void testWishlist();
void testRaport();
void testExporta();
void testUndo();