#include "Produse_Model.h"
#include <QtWidgets/QApplication>
#include "produs.h"
#include "repo.h"
#include "gui.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    RepoProduse repo{ "produse.txt" };
    ProdusValidator val;
    ServiceProduse serv{ repo, val };
    GUI_Produse gui{ serv };
    test_file();
    gui.show();
    return a.exec();
}
