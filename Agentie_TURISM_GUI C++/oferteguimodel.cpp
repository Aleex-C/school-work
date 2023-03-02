#include "oferteguimodel.h"

void OfertaGUIModel::initializeGUIComponents()
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
	//this->tableOferte = new QTableWidget{ noLines, noColumns };

	//setam header-ul tabelului
	QStringList tblHeaderList;
	//tblHeaderList << "Denumire" << "Desstinatie" << "Tip" << "Pret";
	//this->tableOferte->setHorizontalHeaderLabels(tblHeaderList);

	//optiune pentru a se redimensiona celulele din tabel in functie de continut
	//this->tableOferte->horizontalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
	btnWishlist = new QPushButton{ "Open Wishlist" };
	lyLeft->addWidget(btnWishlist);
	lyRight->addWidget(tableOferte);

	lyMain->addWidget(left);
	lyMain->addWidget(right);
}
void OfertaGUIModel::reloadOfertaList(vector<Oferta> oferte) {
	this->model->setSongs(oferte);
}

void OfertaGUIModel::guiAddOferta() {
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
		int r = this->model->rowCount(QModelIndex());
		this->model->insertRows(r, 1, QModelIndex());
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

void OfertaGUIModel::connectSignalsSlots() {
	QObject::connect(btnAddOferta, &QPushButton::clicked, this, &OfertaGUIModel::guiAddOferta);

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
		auto wishlistWindow = new WishlistGUI{ srv, srv.getWishlist2() };
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

		
		//int r = this->model->rowCount(QModelIndex());
		//this->model->removeRow(tableOferte->currentIndex().row());
		/*QModelIndex index = tableOferte->selectionModel()->selectedRows().at(0);
		this->model->removeRow(index.row(), QModelIndex());*/

		srv.dlt(denumire, destinatie, tip, pret);
		//model->removeRow(0);
		
		/*auto model_nou = new MyTableModel{ srv.getAll() };
		model_nou->setSongs(srv.getAll());
		tableOferte->setModel(model_nou);*/

		//this->reloadOfertaList(this->srv.getAll());

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
	QObject::connect(tableOferte->selectionModel(), &QItemSelectionModel::selectionChanged, [&]() {
		if (tableOferte->selectionModel()->selectedIndexes().isEmpty())return;
		qDebug() << tableOferte->selectionModel()->selectedIndexes()[0].data(Qt::DisplayRole).toString();
		Oferta o = srv.find(tableOferte->selectionModel()->selectedIndexes()[0].data(Qt::UserRole).toString().toStdString());
		editDenumire->setText(QString::fromStdString(o.getDenumire()));
		editDestinatie->setText(QString::fromStdString(o.getDestinatie()));
		editPret->setText(QString::number(o.getPret()));
		editTip->setText(QString::fromStdString(o.getTip()));
		old_dest = editDestinatie->text().toStdString();
		old_den = editDenumire->text().toStdString();
		old_tip = editTip->text().toStdString();
		old_pret = editPret->text().toInt();

		//sau data se pune in edit cu Qt::DisplayRole

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
