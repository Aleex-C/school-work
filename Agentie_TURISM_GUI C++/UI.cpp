#include "UI.h"
#include <iostream>
using std::cin;
using std::cout;
void print(const Oferta& oferta) {
	cout << "<" << oferta.getDenumire() << "> ->";
	cout << "[" << oferta.getDestinatie() << "] ";
	cout << "(" << oferta.getTip() << ") ";
	cout << "*" << oferta.getPret() << "*\n";
}
void print_offers(const vector<Oferta>& lista) {
	for (const Oferta& oferta : lista) {
		cout << "<" << oferta.getDenumire() << "> ->";
		cout << "[" << oferta.getDestinatie() << "] ";
		cout << "(" << oferta.getTip() << ") ";
		cout << "*" << oferta.getPret() << "*\n";
	}
}
void UI::ui_dlt() {
	string denumire;
	string destinatie;
	string tip;
	int pret;
	cout << "Citeste denumire: \n";
	cin >> denumire;
	cout << "Citeste destinatie: \n";
	cin >> destinatie;
	cout << "Citeste tip: \n";
	cin >> tip;
	cout << "Citeste pret: \n";
	cin >> pret;
	if (serv.dlt(denumire, destinatie, tip, pret) == 0) {
		cout << "Oferta stearsa!\n";
	}
	else {
		cout << "Oferta nu a fost gasita!\n";
	}
}

void UI::ui_modify(){
	string denumire;
	string destinatie;
	string tip;
	int pret;
	string denumire_n;
	string destinatie_n;
	string tip_n;
	int pret_n;
	cout << "Citeste denumire vechi: \n";
	cin >> denumire;
	cout << "Citeste destinatie vechi: \n";
	cin >> destinatie;
	cout << "Citeste tip vechi: \n";
	cin >> tip;
	cout << "Citeste pret vechi: \n";
	cin >> pret;
	cout << "Citeste denumire nou: \n";
	cin >> denumire_n;
	cout << "Citeste destinatie nou: \n";
	cin >> destinatie_n;
	cout << "Citeste tip nou: \n";
	cin >> tip_n;
	cout << "Citeste pret nou: \n";
	cin >> pret_n;
	try {
		serv.modify(denumire, destinatie, tip, pret, denumire_n, destinatie_n, tip_n, pret_n);
		cout << "Oferta modificata!\n";
	}
	catch (RepoException& ex) {
		cout << ex.getMessage();
	}
	catch (ValidationException& val) {
		cout << val.getEM();
	}
}

void UI::ui_find(){
	string denumire;
	cout << "Cauta denumire: \n";
	cin >> denumire;
	try {
		print(serv.find(denumire));
	}
	catch (RepoException& re) {
		cout << re.getMessage();
	}
	

}

void UI::ui_filter(){
	string filtru;
	cout << "Citeste filtru: destinatie sau pret\n";
	cin >> filtru;
	if (filtru == "destinatie"){
		cout << "Introduceti destinatia cautata: \n";
		string dest;
		cin >> dest;
		print_offers(serv.dest_filter(dest));
		
	}
	else if (filtru == "pret") {
		cout << "Introduceti pretul cautat: \n";
		int pret;
		cin >> pret;
		print_offers(serv.pret_filter(pret));
	}
	else {
		cout << "Filtru invalid!\n";
	}
}

void UI::ui_sort(){
	cout << "Introduceti sortarea: \n";
	string sortare;
	cin >> sortare;
	if (sortare == "denumire") {
		print_offers(serv.sortedDenumire());
	}
	else if (sortare == "destinatie") {
		print_offers(serv.sortedDestinatie());
	}
	else if (sortare == "tip+pret") {
		print_offers(serv.sortedTipPret());
	}
	else {
		cout << "Sortare invalida!";
	}

}

void UI::printMenu(){
	cout << "\nMENU" << '\n' << "=========" << '\n';
	cout << "1. Adauga oferta: \n2. Print:\n3. Sterge:\n4. Modifica: \n5. Find(denumire): \n6. Filter (destinatie || pret): \n7. Sort (denumire, destinatie, tip+pret):\n8. Meniu Wishlist \n0. Exit!\n >>";

}

void UI::printWishlist(){
	cout << "MENIU WISHLIST" << '\n';
	cout << "1. Adauga oferta in wishlist" << '\n';
	cout << "2. Adauga oferte random in wishlist" << '\n';
	cout << "3. Goleste wishlist" << '\n';
	cout << "4. Afiseaza wishlist curent" << '\n';
	cout << "5. Inapoi la meniul principal" << '\n';
}

void UI::uiWishlist(){
	int cmd = 0;
	int run = 1;
	while (run) {
		printWishlist();
		cout << "Comanda este:";
		cin >> cmd;
		switch (cmd)
		{
		case 1:
			uiAddToWishlist();
			break;
		case 2:
			uiAddRandomToWishlist();
			break;
		case 3:
			uiEmptyWishlist();
			break;

		case 4:
			print_offers(serv.getWishlistOferte());
			break;
		case 5:
			run = 0;
			break;
		default:
			break;
		}

	}
}

void UI::uiAddToWishlist(){
	string denumire;
	cout << "Denumirea ofertei: \n";
	cin >> denumire;
	try {
		serv.addToWishlist(denumire);
		cout << "Oferta adaugata cu succes in wishlist!\n";
	}
	catch (RepoException& re) {
		cout << re.getMessage();
	}
}

void UI::uiAddRandomToWishlist(){
	int cate;
	cout << "Cate oferte sa se adauge in wishlist: \n";
	cin >> cate;
	const size_t no_adaugate = serv.addRandomToWishlist(cate);
	cout << "S-au adaugat " << no_adaugate << " oferte in wishlist!\n";
}

void UI::uiEmptyWishlist(){
	serv.emptyWishlist();
	cout << "S-au sters toate ofertele din wishlist-ul curent!\n";
}

void UI::uiUndo(){
	try {
		serv.undo();
		cout << "Undo succesful!";
	}
	catch (const OfertaException& ex) {
		cout << ex.getMsg();
	}
}

void UI::startUI(){

	while (true) {
		cout << "\nMENU" << '\n' << "========="<<'\n';
		cout << "1. Adauga oferta: \n2. Print:\n3. Sterge:\n4. Modifica: \n5. Find(denumire): \n6. Filter (destinatie || pret): \n7. Sort (denumire, destinatie, tip+pret): \n9.undo \n0. Exit!\n >>";
		int cmd = 0;
		cin >> cmd;
		if (cmd == 0) {
			break;
		}
		if (cmd == 1) {
			string denumire;
			string destinatie;
			string tip;
			int pret;
			cout << "Citeste denumire: \n";
			cin >> denumire;
			cout << "Citeste destinatie: \n";
			cin >> destinatie;
			cout << "Citeste tip: \n";
			cin >> tip;
			cout << "Citeste pret: \n";
			cin >> pret;
			try {
				serv.add(denumire, destinatie, tip, pret);
				cout << "Oferta adaugata!\n";
			}
			catch (RepoException& ex) {
				cout << ex.getMessage();
			}
			catch (ValidationException& val) {
				cout << val.getEM();
			}
			
		}
		else if (cmd == 2) {
			for (const Oferta& oferta : serv.getAll()) {
				cout << "<" << oferta.getDenumire() << "> ->";
				cout << "[" << oferta.getDestinatie() << "] ";
				cout << "(" << oferta.getTip() << ") ";
				cout << "*" << oferta.getPret() << "*\n";
			}
		}
		else if (cmd == 3) {
			ui_dlt();
		}
		else if (cmd == 4) {
			ui_modify();
		}
		else if (cmd == 5) {
			ui_find();
		}
		else if (cmd == 6) {
			ui_filter();
		}
		else if (cmd == 7) {
			ui_sort();
		}
		else if (cmd == 8) {
			uiWishlist();
		}
		else if (cmd == 9) {
			uiUndo();
		}
				
	}
}
