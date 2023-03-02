class Sorter:
    def sort (self, list, key=lambda x: x, cmp=lambda x,y: x<y, reverse=False):
        pass
    
class MergeSorter(Sorter):
    def __identitate(self, x):
        return x
    def __negatie (self, x):
        return not x    
    def __merge(self, list, key, cmp, operatie, st, mij, dr):
        i = st 
        j = mij+1
        k = st 
        aux = [None]*len(list)
        while i<=mij and j<=dr:
            if operatie(cmp(key(list[i]), key(list[j]))):
                aux[k] = list[i]
                k+=1
                i+=1
            else:
                aux[k] = list [j]
                k+=1
                j+=1
        while i<=mij:
            aux[k] = list[i]
            k+=1
            i+=1
        while j<=dr:
            aux[k]=list[j]
            k+=1
            j+=1
        for i in range(st, dr+1):
            list[i]=aux[i]
    
    def __merge_sort_r(self, list, key, cmp, operatie, st, dr):
        if st<dr:
            mij = (st+dr)//2
            self.__merge_sort_r(list, key, cmp, operatie, st, mij)
            self.__merge_sort_r(list, key, cmp, operatie, mij+1, dr)
            self.__merge(list, key, cmp, operatie,st, mij, dr)
    
    
    def sort(self, list, key=lambda x:x, cmp=lambda x, y:x < y, reverse=False):
        st = 0
        dr = len(list)-1
        if reverse:
            operatie = self.__negatie
        else:
            operatie = self.__identitate
        self.__merge_sort_r(list, key, cmp, operatie, st, dr)

class BingoSorter(Sorter):
    def __identitate(self, x):
        return x
    def __negatie (self, x):
        return not x
    def __bingo_sort(self, list, key, min_value, max_value):
        bingo = key(min_value)
        idx = 0
        next_bingo = key(max_value)
        while bingo < key(max_value):
            poz_start = idx
            for i in range(poz_start,len(list)):
                if key(list[i])==bingo:
                    temp = list[i]
                    list[i] = list[idx]
                    list[idx] = temp
                    idx+=1
                elif key(list[i])<next_bingo:
                    next_bingo = key(list[i])
            bingo = next_bingo
            next_bingo = key(max_value)
                                    
    
    
    def sort(self, list, key=lambda x:x, cmp=lambda x, y:x < y, reverse=False):
        mn = min(list, key=lambda x: key(x))
        mx = max(list, key=lambda x: key(x))
        self.__bingo_sort(list, key, mn, mx)
        if reverse:
            list.reverse()
        if cmp(1,2)!=True:
            list.reverse()


