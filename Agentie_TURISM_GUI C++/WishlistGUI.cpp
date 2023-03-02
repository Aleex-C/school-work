#include "WishlistGUI.h"

set<string> WishlistGUI::getTip(const vector<Oferta>& wishlistOferte){
	set<string> tips;

	for (const auto& s : wishlistOferte) {
		tips.insert(s.getTip());
	}
	return tips;
}

int howManyWithTip(const vector<Oferta>& oferte, string tip) {
	int nooff = count_if(oferte.begin(), oferte.end(), [&](Oferta o) {
		return o.getTip() == tip; });
	return nooff;
}
void clearLayout(QLayout* layout) {
	if (layout == NULL)
		return;
	QLayoutItem* item;
	while ((item = layout->takeAt(0))) {
		if (item->layout()) {
			clearLayout(item->layout());
			delete item->layout();
		}
		if (item->widget()) {
			delete item->widget();
		}
		delete item;
	}
	
}
void WishlistGUI::reloadDynamicButtons() {
	clearLayout(this->lyBtnDynamic);
	const vector<Oferta>& wishlistOferte = this->srv.getWishlistOferte();
	set<string> tips = this->getTip(wishlistOferte);

	for (string tip : tips) {
		QPushButton* btn = new QPushButton{ QString::fromStdString(tip) };
		lyBtnDynamic->addWidget(btn);
		int howMany = howManyWithTip(wishlistOferte, tip);
		QObject::connect(btn, &QPushButton::clicked, [=]() {
			QMessageBox::information(this, "Info", QString::fromStdString("Oferte cu tipul " + tip + " : " + to_string(howMany)));

			});
	}
}


void WishlistGUI::initGUI(){
	lyMain = new QHBoxLayout{};
	this->setLayout(lyMain);

	QWidget* leftSide = new QWidget{};
	QVBoxLayout* lyLeft = new QVBoxLayout{};
	leftSide->setLayout(lyLeft);

	QWidget* formW = new QWidget{};
	QFormLayout* lyEdits = new QFormLayout{};
	lblDenumire = new QLabel{ "Denumire" };
	editDenumire = new QLineEdit{};
	lblGenerate = new QLabel{ "Nr. oferte de generat: " };
	editGenerate = new QLineEdit{};

	lyEdits->addRow(lblDenumire, editDenumire);
	lyEdits->addRow(lblGenerate, editGenerate);
	formW->setLayout(lyEdits);

	btnAdd = new QPushButton{ "Adauga in wishlist" };
	btnGenerate = new QPushButton{ "Genereaza random" };
	btnEmpty = new QPushButton{ "Goleste wishlist" };
	//btnExport = new QPushButton{ "Export wishlist" };
	btnClose = new QPushButton{ "Close" };
	btnLabel = new QPushButton{ "Fereastra counter" };
	btnPaint = new QPushButton{ "Paint!" };
	btnLabel->setStyleSheet("background-color: red");

	lyLeft->addWidget(formW);
	lyLeft->addWidget(btnAdd);
	lyLeft->addWidget(btnGenerate);
	lyLeft->addWidget(btnEmpty);
	//lyLeft->addWidget(btnExport);
	lyLeft->addWidget(btnPaint);
	lyLeft->addWidget(btnClose);
	lyLeft->addWidget(btnLabel);

	QWidget* rightSide = new QWidget{};
	QVBoxLayout* lyRight = new QVBoxLayout{};
	rightSide->setLayout(lyRight);

	oferteList = new QListWidget{};
	oferteList->setFixedWidth(320);
	oferteList->setSelectionMode(QAbstractItemView::SingleSelection);

	lyRight->addWidget(oferteList);

	widgetDynamic = new QWidget{};
	lyBtnDynamic = new QVBoxLayout{};
	widgetDynamic->setLayout(lyBtnDynamic);

	reloadDynamicButtons();
	

	lyMain->addWidget(leftSide);
	lyMain->addWidget(rightSide);
	lyMain->addWidget(widgetDynamic);

}

void WishlistGUI::connectSingalsSlots(){
	wishlist.addObserver(this);
	QObject::connect(btnAdd, &QPushButton::clicked, this, &WishlistGUI::addToWishlist);
	QObject::connect(btnGenerate, &QPushButton::clicked, [&]() {
		int nooffs = this->editGenerate->text().toInt();
		qDebug() << "This many offers to add:" << nooffs;
		int howManyAdded = srv.addRandomToWishlist(nooffs);
		this->reloadWishlist();
		this->update();
		});
	/*QObject::connect(btnExport, &QPushButton::clicked, [&]() {

		});*/
	QObject::connect(btnClose, &QPushButton::clicked, this, &WishlistGUI::close);
	QObject::connect(oferteList, &QListWidget::itemSelectionChanged, [&]() {
		auto selItms = oferteList->selectedItems();
		for (auto item : selItms) {
			qDebug() << item->text();
			//item->setBackground(Qt::green); // sets green background
		}

		});
	QObject::connect(btnEmpty, &QPushButton::clicked, [&]() {
		srv.emptyWishlist();
		this->reloadWishlist();
		});
	QObject::connect(btnLabel, &QPushButton::clicked, [&]() {
		auto ofertacounter = new OfertaCounter(srv.getWishlist2());
		ofertacounter->show();
		});
	QObject::connect(btnPaint, &QPushButton::clicked, [&]() {
		auto oferta_paint = new OfertaDraw(srv.getWishlist2());
		oferta_paint->show();
		});

}

void WishlistGUI::reloadWishlist(){
	this->oferteList->clear();

	const vector<Oferta>& oferte = srv.getWishlistOferte();
	for (auto& oferta : oferte) {
		QString currentItem = QString::fromStdString(oferta.getDenumire() + "\t" + oferta.getDestinatie() + "\t" + oferta.getTip() + "\t" + to_string(oferta.getPret()));
		this->oferteList->addItem(currentItem);
	}
	reloadDynamicButtons();
}

void WishlistGUI::addToWishlist(){
	try {
		string titlu = editDenumire->text().toStdString();

		editDenumire->clear();


		this->srv.addToWishlist(titlu);
		this->reloadWishlist();

		//afisam un mesaj pentru a anunta utilizatorul ca melodia s-a adaugat
		QMessageBox::information(this, "Info", QString::fromStdString("oferta adaugata cu succes."));

	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getMessage()));
	}
	catch (ValidationException& ve) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(ve.getEM()));
	}
}
