#pragma once
#include "oferta.h"
#include "repo.h"
class ActiuneUndo {
public:
	virtual void doUndo() = 0;
	//destructorul e virtual pentru a ne asigura ca daca dau delete se apeleaza destructorul din clasa care trebuie
	virtual ~ActiuneUndo() = default;
};

class UndoAdauga : public ActiuneUndo {
	Oferta added_of;
	OfertaRepo& rep;
public:
	UndoAdauga(OfertaRepo& rep, const  Oferta& of) :rep{ rep }, added_of{ of } {}
	void doUndo() override {
		rep.sterge(added_of);
	}
};

class UndoSterge : public ActiuneUndo {
	Oferta deleted_of;
	OfertaRepo& rep;
public:
	UndoSterge(OfertaRepo& rep, const  Oferta& of) :rep{ rep }, deleted_of{ of } {}
	void doUndo() override {
		rep.store(deleted_of);
	}
};
class UndoModifica : public ActiuneUndo {
	Oferta of_v;
	Oferta of_n;
	OfertaRepo& repo;
public:
	UndoModifica(Oferta of_v, Oferta of_n, OfertaRepo& rep) : of_v{ of_v }, of_n{ of_n }, repo{ rep }
	{};
	void doUndo() override {
		repo.modifica(of_n, of_v);
	}
};