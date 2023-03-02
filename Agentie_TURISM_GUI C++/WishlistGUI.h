#pragma once
#include <QtWidgets/QApplication>
#include <QWindow>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <QGridLayout>
#include <QWidget>
#include <QListWidget>
#include <QTableWidget>
#include <QPushButton>
#include <QLabel>
#include <QLineEdit>
#include <QGroupBox>
#include <QFormLayout>
#include "service.h"
#include <QMessageBox>
#include <string>
#include <set>
#include <vector>
#include <QDebug>
#include <QPainter>
#include <cstdlib>
#include "Observer.h"

using std::to_string;
using std::set;	
using std::vector;

class WishlistGUI : public QWidget, public Observer {
private:
	OferteService& srv;
	QHBoxLayout* lyMain;
	QListWidget* oferteList;
	Wishlist& wishlist;

	QLabel* lblDenumire;
	QLineEdit* editDenumire;
	QLineEdit* editGenerate;
	QLabel* lblGenerate;

	QPushButton* btnAdd;
	QPushButton* btnGenerate;
	QPushButton* btnEmpty;
	QPushButton* btnLabel;
	QPushButton* btnExport;
	QPushButton* btnClose;
	QPushButton* btnPaint;

	QWidget* widgetDynamic;
	QVBoxLayout* lyBtnDynamic;
	set<string> getTip(const vector<Oferta>& wishlistOferte);
	void reloadDynamicButtons();

	void initGUI();
	void connectSingalsSlots();
	void reloadWishlist();
	void addToWishlist();
public:
	WishlistGUI(OferteService& srv, Wishlist& wishlist) : srv{ srv }, wishlist {wishlist}{
		initGUI();
		connectSingalsSlots();
		//reloadWishlist();
		update();
	}
	void update() override{
		reloadWishlist();
	}
};

class OfertaCounter : public QWidget, public Observer {
private:
	QLineEdit* textbox;
	Wishlist& wishlist;

public:
	OfertaCounter(Wishlist& wish_list) : wishlist{ wish_list } {
		textbox = new QLineEdit;
		QHBoxLayout* layout = new QHBoxLayout;
		setLayout(layout);
		layout->addWidget(textbox);
		wishlist.addObserver(this);
		update();
	}
	void update() override {
		textbox->setText(std::to_string(wishlist.getAllWishlist().size()).c_str());
	}
	~OfertaCounter() {
		wishlist.removeObserver(this);
	}
};

class OfertaDraw : public QWidget, public Observer {
private:
	Wishlist& wishlist;
protected:
	void paintEvent(QPaintEvent* ev) override {
		int x = 10, y = 10, w = 10;
		QPainter g{ this };
		g.setPen(Qt::blue);
		for (const auto& oferta : wishlist.getAllWishlist())
		{
			g.drawRect(x, y, w, oferta.getPret() / 10);
			//g.drawRect(rand() % 100, rand() % 100, rand() % 100, oferta.getPret() / 10);
			x += 40;
		}
	}
public:
	OfertaDraw(Wishlist& wishlist) : wishlist{ wishlist } {
		wishlist.addObserver(this);
		update();
	}
	void update() override {
		this->repaint();
	}
};