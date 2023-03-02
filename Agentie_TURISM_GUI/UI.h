#pragma once
#include "service.h"
class UI {
	OferteService& serv;
public:
	UI (OferteService& service) noexcept: serv{service}{
	}
	UI(const UI& ui) = delete;
	UI() = default;
	void startUI();
	void ui_dlt();
	void ui_modify();
	void ui_find();
	void ui_filter();
	void ui_sort();
	void printMenu();
	void printWishlist();
	void uiWishlist();
	void uiAddToWishlist();
	void uiAddRandomToWishlist();
	void uiEmptyWishlist();
	void uiUndo();
};
