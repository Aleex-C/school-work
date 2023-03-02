#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_Agentie_TURISM_GUI.h"

class Agentie_TURISM_GUI : public QMainWindow
{
    Q_OBJECT

public:
    Agentie_TURISM_GUI(QWidget *parent = Q_NULLPTR);

private:
    Ui::Agentie_TURISM_GUIClass ui;
};
