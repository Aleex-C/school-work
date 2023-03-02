#include "oferta.h"

const string& Oferta::getDenumire() const noexcept
{
    return denumire;
}

const string& Oferta::getDestinatie() const noexcept
{
    return destinatie;
}

const string& Oferta::getTip() const  noexcept
{
    return tip;
}

int Oferta::getPret() const noexcept 
{
    return pret;
}


void test_getters() {
    Oferta o{ "Baiut", "Baia Mare", "Paris", 100 };
    assert(strcmp(o.getDenumire().c_str(), "Baiut") == 0);
    assert(strcmp(o.getDestinatie().c_str(), "Baia Mare") == 0);
    assert(strcmp(o.getTip().c_str(), "Paris") == 0);
    assert(o.getPret() == 100);
}
bool cmpDenumire(const Oferta& o1, const Oferta& o2) noexcept {
    return o1.getDenumire() < o2.getDenumire();
}
bool cmpDestinatie(const Oferta& o1, const Oferta& o2) noexcept {
    return o1.getDestinatie() < o2.getDestinatie();
}
bool cmpTipPret(const Oferta& o1, const Oferta& o2) noexcept {
    if (o1.getTip() == o2.getTip())
        return o1.getPret() < o2.getPret();
    else
        return o1.getTip() < o2.getTip();
}
