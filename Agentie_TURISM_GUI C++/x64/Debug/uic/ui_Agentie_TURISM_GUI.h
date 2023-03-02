/********************************************************************************
** Form generated from reading UI file 'Agentie_TURISM_GUI.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AGENTIE_TURISM_GUI_H
#define UI_AGENTIE_TURISM_GUI_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Agentie_TURISM_GUIClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *Agentie_TURISM_GUIClass)
    {
        if (Agentie_TURISM_GUIClass->objectName().isEmpty())
            Agentie_TURISM_GUIClass->setObjectName(QString::fromUtf8("Agentie_TURISM_GUIClass"));
        Agentie_TURISM_GUIClass->resize(600, 400);
        menuBar = new QMenuBar(Agentie_TURISM_GUIClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        Agentie_TURISM_GUIClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(Agentie_TURISM_GUIClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        Agentie_TURISM_GUIClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(Agentie_TURISM_GUIClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        Agentie_TURISM_GUIClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(Agentie_TURISM_GUIClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        Agentie_TURISM_GUIClass->setStatusBar(statusBar);

        retranslateUi(Agentie_TURISM_GUIClass);

        QMetaObject::connectSlotsByName(Agentie_TURISM_GUIClass);
    } // setupUi

    void retranslateUi(QMainWindow *Agentie_TURISM_GUIClass)
    {
        Agentie_TURISM_GUIClass->setWindowTitle(QCoreApplication::translate("Agentie_TURISM_GUIClass", "Agentie_TURISM_GUI", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Agentie_TURISM_GUIClass: public Ui_Agentie_TURISM_GUIClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AGENTIE_TURISM_GUI_H
