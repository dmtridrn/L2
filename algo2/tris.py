def fusion(t1, t2):
    resultat = [0] * (len(t1) + len(t2))
    i = j = k = 0

    while i < len(t1) and j < len(t2):
        if t1[i] <= t2[j]:
            resultat[k] = t1[i]
            i += 1
        else:
            resultat[k] = t2[j]
            j += 1
        k += 1

    while i < len(t1):
        resultat[k] = t1[i]
        i += 1
        k += 1

    while j < len(t2):
        resultat[k] = t2[j]
        j += 1
        k += 1

    return resultat

def mergeSort(t, debut, fin):
    if fin - debut <=1:
        return t[debut:fin]
    else:
        milieu = (debut + fin) // 2
        gauche = mergeSort(t,debut,milieu)
        droite = mergeSort(t,milieu,fin)
        return fusion(gauche,droite)
    


def partition(t, debut, fin):
    pivot, gauche, droite = t[debut], debut + 1, fin -1

    while gauche <= droite:
        if t[gauche] <= pivot:
            gauche += 1
        elif t[droite] >= pivot:
            droite -= 1
        else:
            t[gauche], t[droite] = t[droite], t[gauche]

    t[debut], t[droite] = t[droite], t[debut]
    return droite

def quickSort(t, deb = 0, fin = None):
    if fin is None:
        fin = len(t)

    if fin - deb < 2:
        return
    
    pivot = partition(t,deb,fin)
    quickSort(t,deb, pivot)
    quickSort(t, pivot + 1, fin)
    return t

def quickselect(t, k, debut=0, fin=None):
    if fin is None:
        fin = len(t)
    
    if fin - debut <= 1:
        return t[debut]
    
    pivot_idx = partition(t, debut, fin)
    
    pos = pivot_idx - debut
    
    if pos == k - 1:
        return t[pivot_idx]
    elif pos > k - 1:
        return quickselect(t, k, debut, pivot_idx)
    else:
        return quickselect(t, k - pos - 1, pivot_idx + 1, fin)
    
def rechercheDicho(t,k):
    deb = 0
    fin = len(t) - 1
    while deb <= fin:
        mid = (deb+fin)//2
        if t[mid] == k:
            return mid
        elif t[mid] < k:
            deb = mid + 1
        else:
            fin = mid - 1
    return None

def triDrapeau(t):
    bleu = 0 
    blanc = 0
    rouge = len(t) - 1 
    
    while blanc <= rouge:
        if t[blanc] == 0:
            t[bleu], t[blanc] = t[blanc], t[bleu]
            bleu += 1
            blanc += 1
        elif t[blanc] == 1:
            blanc += 1
        else:
            t[blanc], t[rouge] = t[rouge], t[blanc]
            rouge -= 1
    return t

a = [0,2,1,2,0,1,1,0,2,0,1,2,0,1,2,0]
print(triDrapeau(a))