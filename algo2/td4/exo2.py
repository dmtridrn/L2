def occurence_naif(tab, x):
    cpt = 0
    for i in tab:
        if i == x:
            cpt += 1
    return cpt

def trouvePremier(tab, x, debut=0, fin=None):
    if fin is None:
        fin = len(tab) - 1
    while debut <= fin:
        mid = (debut + fin) // 2
        if (mid == 0 or tab[mid-1] < x) and tab[mid] == x:
            return mid
        elif tab[mid] < x:
            debut = mid + 1
        else:
            fin = mid - 1
    return None

def trouverDernier(tab, x, debut=0, fin=None):
    if fin is None:
        fin = len(tab) - 1
    while debut <= fin:
        mid = (debut + fin) // 2
        if (mid == 0 or tab[mid+1] > x) and tab[mid] == x:
            return mid
        elif tab[mid] <= x:
            debut = mid + 1
        else:
            fin = mid - 1
    return None

def occurenceDicho(T,x):
    premier = trouvePremier(T,x)
    dernier = trouverDernier(T,x)
    return dernier-premier + 1

tab = [1,3,5,5,5,5,5,5,5,8,9,12,16,26,61]


print(trouvePremier(tab, 5))
print(trouverDernier(tab, 5))
print(occurenceDicho(tab,5))

    