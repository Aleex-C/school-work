#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Produse_Model.h"

class Produse_Model : public QMainWindow
{
    Q_OBJECT

public:
    Produse_Model(QWidget *parent = nullptr);
    ~Produse_Model();

private:
    Ui::Produse_ModelClass ui;
};
