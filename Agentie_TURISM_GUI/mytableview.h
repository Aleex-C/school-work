#pragma once
#include <QAbstractTableModel>
#include <QBrush>
#include <qfont.h>
#include <Qt>
#include "oferta.h"
#include <vector>
#include <qdebug.h>
using std::vector;


class MyTableModel :public QAbstractTableModel {
	std::vector<Oferta> oferte;
public:
	MyTableModel(const std::vector<Oferta>& oferte) :oferte{ oferte } {
	}

	int rowCount(const QModelIndex& parent = QModelIndex()) const override {
		return oferte.size();
	}
	int columnCount(const QModelIndex& parent = QModelIndex()) const override {
		return 4;
	}

	//Returns the data stored under the given role for the item referred to by the index.
	QVariant data(const QModelIndex& index, int role) const override {
		if (role == Qt::DisplayRole) {
			auto oferta = this->oferte[index.row()];
			if (index.column() == 0) {
				return QString::fromStdString(oferta.getDenumire());
			}
			else if (index.column() == 1) {
				return QString::fromStdString(oferta.getDestinatie());
			}
			else if (index.column() == 3) {
				return QString::fromStdString(oferta.getTip());
			}
			else {
				return QString::number(oferta.getPret());
			}
		
		}
		else if (role == Qt::UserRole) {
			auto oferta = this->oferte[index.row()];
			if (index.column() == 0) {
				return QString::fromStdString(oferta.getDenumire());
			}
			else if (index.column() == 1) {
				return QString::fromStdString(oferta.getDenumire());
			}
			else if (index.column() == 3) {
				return QString::fromStdString(oferta.getDenumire());
			}
			else {
				return QString::fromStdString(oferta.getDenumire());
			}
		}
		else if (role == Qt::BackgroundRole) {
			auto oferta = this->oferte[index.row()];
			if (oferta.getDestinatie() == "Suceava") {
				return QBrush(Qt::blue);
			}
		}
		else if (role == Qt::FontRole) {
			auto oferta = this->oferte[index.row()];
			if (oferta.getTip() == "sejur") {
				auto font = QFont();
				font.setBold(true);
				return font;
			}
		}
		else if (role == Qt::ForegroundRole) {
			auto oferta = this->oferte[index.row()];
			if (oferta.getPret() > 400) {
				return QBrush(Qt::green);
			}
		}

		return QVariant{};
	}

	void setSongs(const vector<Oferta> songs) {
		this->oferte = songs;
		auto topIndex = createIndex(0, 0);
		auto bottomIndex = createIndex(songs.size(), 4);
		emit dataChanged(topIndex, bottomIndex);
	}

	Qt::ItemFlags flags(const QModelIndex& /*index*/) const {
		return Qt::ItemIsSelectable | Qt::ItemIsEditable | Qt::ItemIsEnabled;
	}

	bool insertRows(int row, int count, const QModelIndex& parent) override
	{
		beginInsertRows(parent, row, row + count - 1);
		endInsertRows();
		return true;
	}


};
