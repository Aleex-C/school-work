#pragma once
#include "oferta.h"
#include <vector>
#include <algorithm>
#include <random> 
#include "Observer.h"

using std::vector;

class Wishlist: public Observable {
private:
	vector<Oferta> WishlistOferte;
public:
	Wishlist() = default;
	void addOfertaToWishlist(const Oferta& o);
	void emptyWishlist() noexcept;
	void addRandomOferte(vector<Oferta> lista_oferte, int cate);
	const vector<Oferta>& getAllWishlist() const noexcept;
};


