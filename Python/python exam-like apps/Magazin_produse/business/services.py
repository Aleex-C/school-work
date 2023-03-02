from entities.produs import Produs
class ServiceProduse(object):
    def __init__(self, repo_produse, val_produse):
        self.__repo_produse = repo_produse
        self.__val_produse = val_produse
        self.undo_stack = []
    def adauga_produs(self, id_produs, denumire, pret):
        produs = Produs(id_produs, denumire, pret)
        self.__val_produse.validate(produs)
        self.__repo_produse.store(produs)
    def get_all_produse(self):
        return self.__repo_produse.get_produse()
    def delete_by_digit(self, digit):
        rez= []
        undo_stack_produse = []
        produse = self.get_all_produse()
        for produs in produse:
            str_pret = str(produs.get_pret())
            if str(digit) in str_pret:
                rez.append(produs.get_id_produs())
                undo_stack_produse.append(produs)
        self.undo_stack.append(undo_stack_produse)
        for id_remove in rez:
            self.__repo_produse.delete(id_remove)
        return len(rez)
    def filtrare (self, text, price):
        filtered_list = []
        produse = self.get_all_produse()
        for produs in produse:
            if text!=-1 and produs.get_denumire() in text:
                if price!=-1 and produs.get_pret()<price:
                    filtered_list.append(produs)
                else:
                    filtered_list.append(produs)
            elif price!=-1 and produs.get_pret()<price:
                filtered_list.append(produs)
        return filtered_list
    def undo_delete(self):
        if len(self.undo_stack)!=0:
            de_adaugat = self.undo_stack.pop()
            for produs in de_adaugat:
                self.__repo_produse.store(produs)
            return "Successful undo!"
        return "No undos to be seen here!"
           
        


