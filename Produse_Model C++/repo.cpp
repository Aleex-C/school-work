#include "repo.h"

void test_file(){
	RepoProduse repo("test.txt");
	vector<Produs> produse = repo.get_all();
	assert(produse[2].get_id() == 1);
	assert(produse[1].get_nume() == "lapte");
	assert(produse[0].get_tip() == "panificatie");
}
