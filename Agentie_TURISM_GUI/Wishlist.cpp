#include "Wishlist.h"
using std::shuffle;

void Wishlist::addOfertaToWishlist(const Oferta& o){
	this->WishlistOferte.push_back(o);
	notify();
}

void Wishlist::emptyWishlist() noexcept{
	this->WishlistOferte.clear();
	notify();
}

void Wishlist::addRandomOferte(vector<Oferta> lista_oferte, int cate){
	shuffle(lista_oferte.begin(), lista_oferte.end(), std::default_random_engine(std::random_device{}())); //amesteca vectorul lista_oferte
	while (WishlistOferte.size() < cate && lista_oferte.size() > 0) {
		WishlistOferte.push_back(lista_oferte.back());
		lista_oferte.pop_back();
	}
	notify();
}

const vector<Oferta>& Wishlist::getAllWishlist() const noexcept {
	return this->WishlistOferte;
}
