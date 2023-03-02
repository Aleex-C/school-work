#include "OfertaGUI.h"

void OfertaGUI::initializeGUIComponents()
{
	//main layout
	QHBoxLayout* lyMain = new QHBoxLayout;
	this->setLayout(lyMain);

	//left side
	QWidget* left = new QWidget;
	QVBoxLayout* lyLeft = new QVBoxLayout;
	left->setLayout(lyLeft);
	
	//add
	QWidget* form = new QWidget;
	QFormLayout* lyForm = new QFormLayout;
	form->setLayout(lyForm);
	editDenumire = new QLineEdit;
	editDestinatie = new QLineEdit;
	editTip = new QLineEdit;
	editPret = new QLineEdit;
	
	lyForm->addRow(lblDenumire, editDenumire);
	lyForm->addRow(lblDestinatie, editDestinatie);
	lyForm->addRow(lblTip, editTip);
	lyForm->addRow(lblPret, editPret);
	btnAddOferta = new QPushButton("Adauga oferta");
	btnDelete = new QPushButton("Sterge oferta");
	btnModify = new QPushButton("Modifica oferta");
	btnUndo = new QPushButton("UNDO");
	lyForm->addWidget(btnAddOferta);
	lyForm->addWidget(btnDelete);
	lyForm->addWidget(btnModify);
	lyForm->addWidget(btnUndo);
	lyLeft->addWidget(form);

	QVBoxLayout* lyRadioBox = new QVBoxLayout;
	this->groupBox->setLayout(lyRadioBox);
	lyRadioBox->addWidget(SrtDenumire);
	lyRadioBox->addWidget(SrtDestinatie);

	btnSortOferte = new QPushButton("Sorteaza oferte");
	lyRadioBox->addWidget(btnSortOferte);

	lyLeft->addWidget(groupBox);

	QWidget* formFilter = new QWidget;
	QFormLayout* lyFormFilter = new QFormLayout;
	formFilter->setLayout(lyFormFilter);
	editFilterDest = new QLineEdit();
	lyFormFilter->addRow(lblFilterCriteria, editFilterDest);
	btnFilterOferte = new QPushButton("Filtreaza oferte dupa destinatie");
	lyFormFilter->addWidget(btnFilterOferte);

	lyLeft->addWidget(formFilter);

	btnReloadData = new QPushButton("Reload data");
	lyLeft->addWidget(btnReloadData);

	QWidget* right = new QWidget;
	QVBoxLayout* lyRight = new QVBoxLayout;
	right->setLayout(lyRight);

	int noLines = 10;
	int noColumns = 4;
	this->tableOferte = new QTableWidget{ noLines, noColumns };

	//setam header-ul tabelului
	QStringList tblHeaderList;
	tblHeaderList << "Denumire" << "Desstinatie" << "Tip" << "Pret";
	this->tableOferte->setHorizontalHeaderLabels(tblHeaderList);

	//optiune pentru a se redimensiona celulele din tabel in functie de continut
	this->tableOferte->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
	btnWishlist = new QPushButton{ "Open Wishlist" };
	lyLeft->addWidget(btnWishlist);
	lyRight->addWidget(tableOferte);

	lyMain->addWidget(left);
	lyMain->addWidget(right);
}
void OfertaGUI::reloadOfertaList(vector<Oferta> oferte) {
	this->tableOferte->clearContents();
	this->tableOferte->setRowCount(oferte.size());

	int lineNumber = 0;
	for (auto& oferta : oferte) {
		QTableWidgetItem* denumire = new QTableWidgetItem(QString::fromStdString(oferta.getDenumire()));
		auto destinatie = new QTableWidgetItem(QString::fromStdString(oferta.getDestinatie()));
		auto tip = new QTableWidgetItem(QString::fromStdString(oferta.getTip()));
		auto pret = new QTableWidgetItem(QString::number(oferta.getPret()));

		denumire->setData(Qt::UserRole, QString::fromStdString(oferta.getDenumire()));
		destinatie->setData(Qt::UserRole, QString::fromStdString(oferta.getDenumire()));
		tip->setData(Qt::UserRole, QString::fromStdString(oferta.getDenumire()));
		pret->setData(Qt::UserRole, QString::fromStdString(oferta.getDenumire()));

		this->tableOferte->setItem(lineNumber, 0, denumire);
		this->tableOferte->setItem(lineNumber, 1, destinatie);
		this->tableOferte->setItem(lineNumber, 2, tip);
		this->tableOferte->setItem(lineNumber, 3, pret);
		//this->tableOferte->
		lineNumber++;
	}
}

void OfertaGUI::guiAddOferta(){
	try {
		//preluare detalii din QLineEdit-uri
		string denumire = editDenumire->text().toStdString();
		string destinatie = editDestinatie->text().toStdString();
		string tip = editTip->text().toStdString();
		int pret = editPret->text().toInt();

		//optional - golim QLineEdit-urile dupa apasarea butonului
		editDenumire->clear();
		editDestinatie->clear();
		editTip->clear();
		editPret->clear();

		this->srv.add(denumire, destinatie, tip, pret);
		this->reloadOfertaList(this->srv.getAll());

		//afisam un mesaj pentru a anunta utilizatorul ca melodia s-a adaugat
		QMessageBox::information(this, "Info", QString::fromStdString("Oferta adaugata cu succes."));

	}
	catch (RepoException& re) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(re.getMessage()));
	}
	catch (ValidationException& ve) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(ve.getEM()));
	}

}

void OfertaGUI::connectSignalsSlots(){
	QObject::connect(btnAddOferta, &QPushButton::clicked, this, &OfertaGUI::guiAddOferta);

	QObject::connect(btnSortOferte, &QPushButton::clicked, [&]() {
		if (this->SrtDenumire->isChecked())
			this->reloadOfertaList(srv.sortedDenumire());
		else if (this->SrtDestinatie->isChecked())
			this->reloadOfertaList(srv.sortedDestinatie());
		});

	QObject::connect(btnFilterOferte, &QPushButton::clicked, [&]() {
		string filterC = this->editFilterDest->text().toStdString();
		this->reloadOfertaList(srv.dest_filter(filterC));
		});

	QObject::connect(btnReloadData, &QPushButton::clicked, [&]() {
		this->reloadOfertaList(srv.getAll());
		});
	QObject::connect(btnWishlist, &QPushButton::clicked, [&]() {
		auto wishlistWindow = new WishlistGUI{ srv, srv.getWishlist2()};
		wishlistWindow->show();
		});
	QObject::connect(btnDelete, &QPushButton::clicked, [&]() {
		if (editDenumire->text().isEmpty()) return;
		if (editDestinatie->text().isEmpty()) return;
		if (editTip->text().isEmpty()) return;
		if (editTip->text().isEmpty()) return;

		string denumire = editDenumire->text().toStdString();
		string destinatie = editDestinatie->text().toStdString();
		string tip = editTip->text().toStdString();
		int pret = editPret->text().toInt();

		editDenumire->clear();
		editDestinatie->clear();
		editTip->clear();
		editPret->clear();

		srv.dlt(denumire, destinatie, tip, pret);
		this->reloadOfertaList(this->srv.getAll());

		//afisam un mesaj pentru a anunta utilizatorul ca melodia s-a adaugat
		QMessageBox::information(this, "Info", QString::fromStdString("Oferta stearsa cu succes!"));
		});
	QObject::connect(btnModify, &QPushButton::clicked, [&]() {
		if (editDenumire->text().isEmpty()) return;
		if (editDestinatie->text().isEmpty()) return;
		if (editTip->text().isEmpty()) return;
		if (editTip->text().isEmpty()) return;
		//Oferta o = srv.find(tableOferte->selectedItems()[0]->data(Qt::UserRole).toString().toStdString());
		string new_dest = editDestinatie->text().toStdString();
		string new_den = editDenumire->text().toStdString();
		string new_tip = editTip->text().toStdString();
		int new_pret = editPret->text().toInt();

		editDenumire->clear();
		editDestinatie->clear();
		editTip->clear();
		editPret->clear();

		srv.modify(old_den, old_dest, old_tip, old_pret, new_den, new_dest, new_tip, new_pret);
		reloadOfertaList(srv.getAll());
		});
	QObject::connect(tableOferte, &QTableWidget::itemSelectionChanged, [&]() {
		if (tableOferte->selectedItems().isEmpty())return;
		qDebug() << tableOferte->selectedItems()[0]->data(Qt::UserRole).toString();
		Oferta o = srv.find(tableOferte->selectedItems()[0]->data(Qt::UserRole).toString().toStdString());
		editDenumire->setText(QString::fromStdString(o.getDenumire()));
		editDestinatie->setText(QString::fromStdString(o.getDestinatie()));
		editPret->setText(QString::number(o.getPret()));
		editTip->setText(QString::fromStdString(o.getTip()));
		old_dest = editDestinatie->text().toStdString();
		old_den = editDenumire->text().toStdString();
		old_tip = editTip->text().toStdString();
		old_pret = editPret->text().toInt();

		});
	QObject::connect(btnUndo, &QPushButton::clicked, [&]() {
		try {
			srv.undo();
			reloadOfertaList(srv.getAll());
		}
		catch (OfertaException& oe) {
			QMessageBox::warning(this, "Warning", QString::fromStdString(oe.getMsg()));
		}
		});
}
