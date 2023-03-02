#include "service.h"
#include <assert.h>
#include <vector>

int OferteService::add(string denumire, string destinatie, string tip, int pret) {
	Oferta o{ denumire, destinatie, tip, pret };
	val.valideaza(o);
	repo.store(o);
	undoList.push_back(std::make_unique<UndoAdauga>(repo, o));
	return 0;
}

int OferteService::dlt(string dnm, string dest, string tp, int pret) {
	const vector <Oferta>& oferte = getAll();
	int idx = 0;
	for (auto& o : oferte) {
		if (o.getDenumire() == dnm && o.getDestinatie() == dest && o.getPret() == pret && o.getTip() == tp) {
			undoList.push_back(std::make_unique<UndoSterge>(repo, o));
			repo.remove(idx);
			return 0;
		}
		idx++;
	}
	throw RepoException("Oferta nu se afla in lista!");
}

int OferteService::modify(string dnm, string dest, string tp, int pret, string dnm_n, string dest_n, string tp_n, int pret_n) {
	Oferta of_v{ dnm, dest,tp, pret };
	Oferta of_n{ dnm_n, dest_n, tp_n, pret_n };
	repo.modifica(of_v, of_n);
	undoList.push_back(std::make_unique<UndoModifica>(of_v, of_n, repo));
	return 0;
}
const vector<Oferta>& OferteService::getWishlistOferte() noexcept {
	return wish.getAllWishlist();
}

const Oferta& OferteService::find(string denumire) const{
		const auto& cautat = repo.find_repo(denumire);
		return cautat;
}

vector<Oferta> OferteService::filter(std::function<bool(const Oferta&)> fct){
	const vector<Oferta>& allOferte = getAll();
	vector<Oferta> oferte_filtr;
	std::copy_if(allOferte.begin(), allOferte.end(), back_inserter(oferte_filtr),
		fct);
	return oferte_filtr;
}

vector<Oferta> OferteService::dest_filter(string dest){
	return filter([dest](const Oferta& o) noexcept {
		return o.getDestinatie() == dest;
		}) ;
}
vector<Oferta> OferteService::pret_filter(int pret) {
	return filter([pret](const Oferta& o) noexcept {
		return o.getPret() == pret;
		});
}

vector<Oferta> OferteService::sortedDenumire(){
	auto sorted = repo.getAll();
	sort(sorted.begin(), sorted.end(), cmpDenumire);
	//return generalSort(cmpDenumire);
	return sorted;
}

vector<Oferta> OferteService::sortedDestinatie(){
	auto sorted = repo.getAll();
	sort(sorted.begin(), sorted.end(), cmpDestinatie);
//return generalSort(cmpDestinatie);
	return sorted;
}

vector<Oferta> OferteService::sortedTipPret(){
	auto sorted = repo.getAll();
	sort(sorted.begin(), sorted.end(), cmpTipPret);
	//return generalSort(cmpTipPret);
	return sorted;
}

void OferteService::addToWishlist(string denumire){
	const auto& oferta = repo.find_repo(denumire);
	wish.addOfertaToWishlist(oferta);
}

const size_t OferteService::addRandomToWishlist(int cate){
	wish.emptyWishlist();
	wish.addRandomOferte(this->getAll(), cate);
	return wish.getAllWishlist().size();
}

void OferteService::emptyWishlist() noexcept {
	wish.emptyWishlist();
}

map<const int, size_t> OferteService::rapoarte_Pret(){
	const auto oferte = getAll();
	map <const int, size_t> raport;
	for (const auto& o : oferte) {
		size_t count = raport.count(o.getPret());
		if (count == 0) {
			count++;
			raport.insert(pair<const int, size_t>(o.getPret(), count)); //raport[o.getPret()]=count;
		}
		else {
			auto new_count = raport[o.getPret()];
			raport.erase(o.getPret());
			new_count++;
			raport.insert(pair<const int, size_t>(o.getPret(), new_count));
		}
	}
	return raport;
}

void OferteService::exportaCosCVS(string fName) const{
	exportToCVS(fName, wish.getAllWishlist());
}

void OferteService::undo(){
	if (undoList.empty()) {
		throw OfertaException("Nu mai exista operatii de efectuat!");
	}
	undoList.back()->doUndo();
	undoList.pop_back();
}

/*vector<Oferta> OferteService::generalSort(bool(*maiMicF)(const Oferta&, const Oferta&)) {
	vector<Oferta> v{ repo.getAll() };
	for (int i = 0; i < v.size(); i++) {
		for (int j = i + 1; j < v.size(); j++) {
			if (!maiMicF(v.get(i), v.get(j))) {
				//interschimbam
				v.swap(i, j);
			}
		}
	}
	return v;
}*/

#include <fstream>
void testExporta() {
	OfertaRepo rep;
	OfertaValidator val;
	OferteService ctr{ rep, val };
	ctr.add("aaa", "bbb", "ccc", 3);
	ctr.add("ccc", "bbb", "aaa", 2);
	ctr.add("bbb", "bbb", "bbb", 1);
	ctr.addRandomToWishlist(3);
	ctr.exportaCosCVS("testExport.cvs");
	std::ifstream in("testExport.cvs");
	assert(in.is_open());
	int countLines = 0;
	while (!in.eof()) {
		string line;
		in >> line;
		countLines++;
	}
	in.close();
	assert(countLines == 4);//avem o linie pentru fiecare pet + o linie goala

	//daca se da un nume de fisier invalid se arunca exceptie
	try {
		ctr.exportaCosCVS("test/Export.cvs");
		assert(false);
	}
	catch (OfertaException&) {
		assert(true);
	}
}

void testAdd(){
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "A", "C", 200);
	const auto& oferte = service.getAll();
	assert(oferte.size() == 1);
}
void testRemove() {
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "A", "C", 200);
	service.dlt("A", "A", "C", 200);
	const auto& oferte = service.getAll();
	assert(oferte.size() == 0);
	try {
		service.dlt("B", "C", "D", 200);
		assert(false);
	}
	catch (RepoException) {
		assert(true);
	}
}

void testModify(){
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "A", "C", 200);
	service.modify("A", "A", "C", 200, "B", "B", "D", 500);
	const auto& oferte = service.getAll();
	assert(oferte.size() == 1);
	for (const Oferta& o : oferte) {
		assert(o.getPret() == 500);
	}

}
void testFind() {
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "A", "C", 200);
	try {
		service.find("A");
		assert(true);
	}
	catch (RepoException) {
		assert(false);
	}
	try {
		service.find("B");
		assert(false);
	}
	catch (RepoException) {
		assert(true);
	}

}

void testFilter(){
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "A", "C", 200);
	service.add("A", "B", "C", 200);
	service.add("B", "A", "C", 400);
	const auto& oferte = service.pret_filter(200);
	assert(oferte.size() == 2);
	const auto& oferte2 = service.dest_filter("A");
	assert(oferte2.size() == 2);
}

void testSort() {
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "C", "gr", 200);
	service.add("B", "B", "gr", 100);
	service.add("C", "A", "h", 400);
	const auto& oferteDenumire = service.sortedDenumire();
	assert(oferteDenumire.at(0).getPret() == 200);
	const auto& oferteDestinatie = service.sortedDestinatie();
	assert(oferteDestinatie.at(0).getPret() == 400);
	const auto& oferteTipPret = service.sortedTipPret();
	assert(oferteTipPret.at(0).getPret() == 100);

}

void testUndo() {
	OfertaRepo rep;
	OfertaValidator val;
	OferteService srv{ rep, val };
	srv.add("a", "b", "c", 1);
	srv.modify("a", "b", "c", 1, "z", "q", "w", 2);
	srv.undo();
	assert(srv.getAll().size() == 1);
	srv.add("b", "b", "c", 1);
	srv.add("c", "b", "c", 1);
	srv.undo();
	assert(srv.getAll().size() == 2);
	srv.undo();
	srv.undo();
	assert(srv.getAll().size() == 0);
	try {
		srv.undo();
		assert(false);
	}
	catch (OfertaException&) {
		assert(true);
	}
	srv.add("d", "b", "c", 1);
	srv.dlt("d", "b", "c", 1);
	srv.undo();
	assert(srv.getAll().size() == 1);
}

void testWishlist() {
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "C", "gr", 200);
	service.add("B", "B", "gr", 100);
	service.add("C", "A", "h", 400);
	service.addToWishlist("A");
	assert(service.getWishlistOferte().size() == 1);
	service.emptyWishlist();
	assert(service.getWishlistOferte().size() == 0);
	service.addRandomToWishlist(5);
	assert(service.getWishlistOferte().size() == 3);
	service.emptyWishlist();
	service.addToWishlist("A");
	service.addToWishlist("B");
	assert(service.getWishlistOferte().size() == 2);
	try {
		service.addToWishlist("D");
		assert(false);
	}
	catch (RepoException&) {
		assert(true);
	}
}

void testRaport(){
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	service.add("A", "C", "gr", 200);
	service.add("B", "B", "gr", 100);
	service.add("C", "A", "h", 400);
	service.add("D", "A", "h", 400);
	service.add("E", "A", "h", 400);
	service.add("F", "A", "h", 400);
	service.add("G", "A", "h", 400);
	map<const int, size_t> raport = service.rapoarte_Pret();
	for (const auto& kv : raport) {
		if (kv.first == 100) {
			assert(kv.second == 1);
		}
		else if (kv.first == 200) {
			assert(kv.second == 1);
		}
		else if (kv.first == 400) {
			assert(kv.second == 5);
		}
	}
}

