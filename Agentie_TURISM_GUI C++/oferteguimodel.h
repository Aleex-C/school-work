#pragma once
#include <qwidget.h>
#include <qlistwidget.h>
#include <qpushbutton.h>
#include <qlineedit.h>
#include <qboxlayout.h>
#include <qdebug.h>
#include "service.h"
#include "oferta.h"
#include <vector>
#include <qlabel.h>
#include <qgroupbox.h>
#include <qradiobutton.h>
#include <qtablewidget.h>
#include <QFormLayout>
#include <qheaderview.h>
#include <qmessagebox.h>
#include "WishlistGUI.h"
#include "mytableview.h"

using std::vector;
using std::string;

class OfertaGUIModel : public QWidget {
private:
	OferteService& srv;
	//WishlistGUI wishlistWindow {srv};
	QLabel* lblDenumire = new QLabel{ "Denumire oferta: " };
	QLabel* lblDestinatie = new QLabel{ "Destinatie oferta: " };
	QLabel* lblTip = new QLabel{ "Tipul ofertei: " };
	QLabel* lblPret = new QLabel{ "Pretul ofertei: " };

	QLineEdit* editDenumire;
	QLineEdit* editDestinatie;
	QLineEdit* editTip;
	QLineEdit* editPret;

	QPushButton* btnAddOferta;

	QGroupBox* groupBox = new QGroupBox(tr("Tip sortare"));

	QRadioButton* SrtDenumire = new QRadioButton(QString::fromStdString("Denumire"));
	QRadioButton* SrtDestinatie = new QRadioButton(QString::fromStdString("Destinatie"));
	QPushButton* btnSortOferte;

	QPushButton* btnReloadData;
	QPushButton* btnDelete;
	QPushButton* btnModify;
	QPushButton* btnUndo;
	string old_dest;
	string old_den;
	string old_tip;
	int old_pret;

	QLabel* lblFilterCriteria = new QLabel{ "Destinatie dupa care se filtreaza:" };
	QLineEdit* editFilterDest;
	QPushButton* btnFilterOferte;
	MyTableModel* model;
	//QTableWidget* tableOferte;
	QTableView* tableOferte = new QTableView;
	QPushButton* btnWishlist;

	void initializeGUIComponents();
	void connectSignalsSlots();
	void reloadOfertaList(vector<Oferta> oferte);
public:
	OfertaGUIModel(OferteService& service) : srv{ service } {
		initializeGUIComponents();
		this->model = new MyTableModel{ this->srv.getAll() };
		tableOferte->setModel(model);
		connectSignalsSlots();
		reloadOfertaList(srv.getAll());
	}
	void guiAddOferta();
};