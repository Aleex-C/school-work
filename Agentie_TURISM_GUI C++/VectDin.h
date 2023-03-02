#pragma once
#define INITIAL_CAPACITY 5

template <typename ElementT>
class IteratorVectorT;

template <typename ElementT>
class VectDyn
{
public:
	/*
	Constructor default
	*/
	VectDyn() noexcept;

	/*
	Copy constructor
	*/
	VectDyn(const VectDyn& ot);

	/*
	Delete
	*/
	~VectDyn();

	/*
	Assign operator 
	*/
	VectDyn& operator=(const VectDyn& ot);


	/*
	Move constructor
	Apelat daca construim un nou VectDyn dintr-un r-value (obiect "temporar", expresie de la return)
	*/
	VectDyn(VectDyn&& ot) noexcept; 

	/*
	Assign movement -> pentru move constructor
	*/
	VectDyn& operator=(VectDyn&& ot); //rule of 5 


	void add(const ElementT& el);
	void erase(int idx) noexcept;
	void swap(int i, int j);

	ElementT& get(int poz) const noexcept;

	void set(int poz, const ElementT& el);

	int size() const noexcept;

	friend class IteratorVectorT<ElementT>;
	IteratorVectorT<ElementT> begin() const noexcept;
	IteratorVectorT<ElementT> end() const noexcept;


private:
	int lg;
	int cap;
	ElementT* elems;

	void capacity();
};

template<typename ElementT>
VectDyn<ElementT>::VectDyn() noexcept :elems{ new ElementT[INITIAL_CAPACITY] }, cap{ INITIAL_CAPACITY }, lg{ 0 } {};
//@TODO: separate !!!
template<typename ElementT>
VectDyn<ElementT>::VectDyn(const VectDyn<ElementT>& ot) {
	elems = new ElementT[ot.cap];
	for (int i = 0; i < ot.lg; i++) {
		elems[i] = ot.elems[i]; 
	}
	lg = ot.lg;
	cap = ot.cap;
}

template<typename ElementT>
VectDyn<ElementT>& VectDyn<ElementT>::operator=(const VectDyn<ElementT>& ot) {
	if (this == &ot) {
		return *this;;
	}
	delete[] elems;
	elems = new ElementT[ot.cap];
	for (int i = 0; i < ot.lg; i++) {
		elems[i] = ot.elems[i]; 
	}
	lg = ot.lg;
	cap = ot.cap;
	return *this;
}

/*
Eliberam memoria
*/
template<typename ElementT>
VectDyn<ElementT>::~VectDyn() {
	delete[] elems;
}

template<typename ElementT>
VectDyn<ElementT>::VectDyn(VectDyn&& ot) noexcept {
	elems = ot.elems;
	lg = ot.lg;
	cap = ot.cap;

	ot.elems = nullptr;
	ot.lg = 0;
	ot.cap = 0;
}

template<typename ElementT>
VectDyn<ElementT>& VectDyn<ElementT>::operator=(VectDyn<ElementT>&& ot) {
	if (this == &ot) {
		return *this;
	}
	delete[] elems;
	elems = ot.elems;
	lg = ot.lg;
	cap = ot.cap;

	ot.elems = nullptr;
	ot.lg = 0;
	ot.cap = 0;
	return *this;
}

template<typename ElementT>
void VectDyn<ElementT>::add(const ElementT& el) {
	capacity();//alocam memorie extra daca e nevoie
	elems[lg++] = el;
}

template<typename ElementT>
void VectDyn<ElementT>::erase(int idx) noexcept{
	for (int i = idx; i <= lg; i++) {
		elems[i] = elems[i + 1];
	}
	lg--;
}

template<typename ElementT>
void VectDyn<ElementT>::swap(int i, int j){
	ElementT aux = elems[i];
	elems[i] = elems[j];
	elems[j] = aux;
}

template<typename ElementT>
ElementT& VectDyn<ElementT>::get(int poz) const noexcept{
	return elems[poz];
}

template<typename ElementT>
void VectDyn<ElementT>::set(int poz, const ElementT& el) {
	elems[poz] = el;
}

template<typename ElementT>
int VectDyn<ElementT>::size() const noexcept {
	return lg;
}

template<typename ElementT>
void VectDyn<ElementT>::capacity() {
	if (lg < cap) {
		return; //mai avem loc
	}
	cap *= 2;
	ElementT* aux = new ElementT[cap];
	for (int i = 0; i < lg; i++) {
		aux[i] = elems[i];
	}
	delete[] elems;
	elems = aux;
}

template<typename ElementT>
IteratorVectorT<ElementT> VectDyn<ElementT>::begin() const noexcept
{
	return IteratorVectorT<ElementT>(*this);
}

template<typename ElementT>
IteratorVectorT<ElementT> VectDyn<ElementT>::end() const noexcept
{
	return IteratorVectorT<ElementT>(*this, lg);
}

template<typename ElementT>
class IteratorVectorT {
private:
	const VectDyn<ElementT>& v;
	int poz = 0;
public:
	IteratorVectorT(const VectDyn<ElementT>& v) noexcept;
	IteratorVectorT(const VectDyn<ElementT>& v, int poz)noexcept;
	bool valid()const;
	ElementT& element() const noexcept;
	void next() noexcept;
	ElementT& operator*() noexcept;
	IteratorVectorT& operator++() noexcept;
	bool operator==(const IteratorVectorT& ot)noexcept;
	bool operator!=(const IteratorVectorT& ot)noexcept;
};

template<typename ElementT>
IteratorVectorT<ElementT>::IteratorVectorT(const VectDyn<ElementT>& v) noexcept :v{ v } {}

template<typename ElementT>
IteratorVectorT<ElementT>::IteratorVectorT(const VectDyn<ElementT>& v, int poz)noexcept : v{ v }, poz{ poz } {}

template<typename ElementT>
bool IteratorVectorT<ElementT>::valid()const {
	return poz < v.lg;
}

template<typename ElementT>
ElementT& IteratorVectorT<ElementT>::element() const noexcept {
	return v.elems[poz];
}

template<typename ElementT>
void IteratorVectorT<ElementT>::next() noexcept{
	poz++;
}

template<typename ElementT>
ElementT& IteratorVectorT<ElementT>::operator*()  noexcept{
	return element();
}

template<typename ElementT>
IteratorVectorT<ElementT>& IteratorVectorT<ElementT>::operator++() noexcept {
	next();
	return *this;
}


template<typename ElementT>
bool IteratorVectorT<ElementT>::operator==(const IteratorVectorT<ElementT>& ot) noexcept {
	return poz == ot.poz;
}

template<typename ElementT>
bool IteratorVectorT<ElementT>::operator!=(const IteratorVectorT<ElementT>& ot) noexcept {
	return !(*this == ot);
}

