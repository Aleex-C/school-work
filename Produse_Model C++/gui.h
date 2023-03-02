#pragma once
#include "service.h"
#include <QWidget>
#include <qtablewidget.h>
#include <qheaderview.h>
#include "MyTableModel.h"
#include <qlabel>
#include <qpushbutton.h>
class GUI_Produse: public QWidget {
private:
	ServiceProduse& service;

	QTableView* tableProduse;
	MyTableModel* model;

	QLineEdit* editID;
	QLineEdit* editNume;
	QLineEdit* editTip;
	QLineEdit* editPret;
	QLineEdit* editValueSlider;

	QLabel* lblValueSlider = new QLabel{ "Valoare slider: " };
	QLabel* lblID = new QLabel{ "ID-ul produsului: " };
	QLabel* lblNume = new QLabel{ "Numele produslui: " };
	QLabel* lblTip = new QLabel{ "Tipul produsului: " };
	QLabel* lblPret = new QLabel{ "Pretul produslui: " };


	QPushButton* btnAddP;
	QSlider* slider;

	void init();
	void connect();
	void reloadProduse();
public:
	GUI_Produse(ServiceProduse& serv) : service{ serv } {
		init();
		reloadProduse();
		connect();
	}
};