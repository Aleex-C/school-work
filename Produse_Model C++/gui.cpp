#include "gui.h"
#include <QHBoxLayout>
#include <qformlayout>
#include <qlineedit>
#include <qmessagebox>

void GUI_Produse::init(){
	QHBoxLayout* lyMain = new QHBoxLayout;
	this->setLayout(lyMain);
	/// <summary>
	/// FORM
	/// </summary>
	QWidget* form = new QWidget;
	QFormLayout* lyForm = new QFormLayout;
	form->setLayout(lyForm);
	editID = new QLineEdit;
	editNume = new QLineEdit;
	editTip = new QLineEdit;
	editPret = new QLineEdit;

	lyForm->addRow(lblID, editID);
	lyForm->addRow(lblNume, editNume);
	lyForm->addRow(lblTip, editTip);
	lyForm->addRow(lblPret, editPret);
	btnAddP = new QPushButton("Adauga produs");
	lyForm->addWidget(btnAddP);
	/// <summary>
	/// left
	/// </summary>
	QWidget* left = new QWidget;
	QVBoxLayout* lyLeft = new QVBoxLayout;
	left->setLayout(lyLeft);

	lyLeft->addWidget(form);

	QWidget* slidersec = new QWidget;
	QHBoxLayout* lySlider = new QHBoxLayout;
	slidersec->setLayout(lySlider);
	lySlider->addWidget(lblValueSlider);
	editValueSlider = new QLineEdit;
	slider = new QSlider{};
	slider->setMinimum(1);
	slider->setMaximum(100);
	lySlider->addWidget(editValueSlider);
	lySlider->addWidget(slider);
	lyLeft->addWidget(slidersec);

	/// <summary>
	/// right
	/// </summary>
	QWidget* right = new QWidget;
	QVBoxLayout* lyRight = new QVBoxLayout;
	right->setLayout(lyRight);
	tableProduse = new QTableView;
	this->tableProduse->setSelectionBehavior(QAbstractItemView::SelectRows);
	model = new MyTableModel(slider,service);

	lyRight->addWidget(tableProduse);
	lyMain->addWidget(left);
	lyMain->addWidget(right);
}

void GUI_Produse::connect(){
	QObject::connect(btnAddP, &QPushButton::clicked, this, [&]() {
		int id = editID->text().toInt();
		string nume = editNume->text().toStdString();
		string tip = editTip->text().toStdString();
		double pret = editPret->text().toDouble();
		editID->clear();
		editNume->clear();
		editTip->clear();
		editPret->clear();
		try {
			service.add(id, nume, tip, pret);
			QMessageBox::information(this, "Info!", "Produs adaugat cu succes!");
			reloadProduse();
		}
		catch (RepoException& re) {
			QMessageBox::information(this, "Warning!", QString::fromStdString(re.getMessage()));
		}
		catch (ValidationError& ve) {
			QMessageBox::information(this, "Warning!", QString::fromStdString(ve.getMsg()));
		}
		});
	QObject::connect(slider, &QSlider::sliderMoved, [&]() {
		editValueSlider->setText(QString::number(slider->value()));
		reloadProduse();
		});

}

void GUI_Produse::reloadProduse(){
	this->tableProduse->setModel(nullptr);
	this->tableProduse->setModel(model);
}
