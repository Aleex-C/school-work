//#define _CRTDBG_MAP_ALLOC
//#include <stdlib.h>
//#include <crtdbg.h>

#include <iostream>
#include "OfertaGUI.h"
#include <QtWidgets/QApplication>
#include <qlabel.h>
#include "oferta.h"
#include "repo.h"
#include "UI.h"
#include "Agentie_TURISM_GUI.h"
#include "oferteguimodel.h"
void run() {
	OfertaRepo repo;
	OfertaValidator val;
	OferteService service{ repo, val };
	UI ui{ service };
	ui.startUI();
}
void runGUI(int argc, char* argv[]) {
	QApplication a(argc, argv);
	RepoFile rep{"oferte.txt"};
	OfertaValidator val;
	OferteService ctr{ rep, val };

	//OfertaGUI gui{ ctr };
	OfertaGUIModel gui{ ctr };
	gui.show();
	a.exec();
}

int main(int argc, char* argv[]) {

	testRepo();
	testAdd();
	test_getters();
	testRemove();
	testModify();
	testFind();
	testFilter();
	testSort();
	testValidator();
	testWishlist();
	testRaport();
	testExporta();
	testUndo();
	//run();
	runGUI(argc, argv);
	//_CrtDumpMemoryLeaks();
	return 0;
}
