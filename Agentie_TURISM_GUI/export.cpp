#include "export.h"
#include <fstream>

void exportToCVS(const std::string& fName, const std::vector<Oferta>& oferte){
		std::ofstream out(fName, std::ios::trunc);
		if (!out.is_open()) {
			throw OfertaException("Unable to open file:" + fName);
		}
		for (const auto& o : oferte) {
			out << o.getDenumire() << ",";
			out << o.getDestinatie() << ",";
			out << o.getPret() << "," ;
			out << o.getTip() << "\n";
		}
		out.close();
}
