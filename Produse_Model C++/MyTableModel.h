#pragma once
#include <QAbstractTableModel>
#include "service.h"
class MyTableModel : public QAbstractTableModel {
private:
	ServiceProduse& service;
	QSlider* slider;
public:
	MyTableModel(QSlider* slider, ServiceProduse& service) : slider{ slider }, service { service } {};
	int rowCount(const QModelIndex& parent = QModelIndex()) const override {
		return this->service.get_all_produse().size();
	}
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {
		return 5;
	}
	QVariant data(const QModelIndex& index, int role = Qt::DisplayRole) const override {
		Produs p = this->service.get_all_produse()[index.row()];
		if(role==Qt::ForegroundRole){
			int pretmaxim = slider->value();
			if (p.get_pret() <= pretmaxim) return QBrush{ Qt::red };
				
		}
		if (role == Qt::DisplayRole) {
			if (index.column() == 0) {
				return QString::fromStdString(std::to_string(p.get_id()));
			}
			if (index.column() == 1){
				return QString::fromStdString(p.get_nume());
			}
			if (index.column() == 2) {
				return QString::fromStdString(p.get_tip());
			}
			if (index.column() == 3) {
				return QString::fromStdString(std::to_string(p.get_pret()));
			}
			if (index.column() == 4) {
				return QString::fromStdString(std::to_string(this->service.nr_vocale(p.get_nume())));
			}
		}
		return QVariant{};
	}
	Qt::ItemFlags item(int section, Qt::Orientation orientation, int role) const
	{
		return Qt::ItemIsEnabled | Qt::ItemIsSelectable | Qt::ItemIsEditable;
	}
	QVariant headerData(int section, Qt::Orientation orientation, int role) const {
		if (role == Qt::DisplayRole)
		{
			if (orientation == Qt::Horizontal)
			{
				if (section == 0)
					return tr("Id");
				if (section == 1)
					return tr("Nume");
				if (section == 2)
					return tr("Tip");
				if (section == 3)
					return tr("Pret");
				if (section == 4)
					return tr("vocale");
				return QString("");
			}
		}
		return QVariant{};
	}
};