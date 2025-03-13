def chercheVainqueur(L):
    max = 0
    vainqueur = 0
    lent = len(L)
    for i in range(lent):
        cpt = 0
        for j in range(lent):
            if L[j] == L[i]:
                cpt +=1
        if cpt > max:
            max = cpt
            vainqueur = L[i]
    return vainqueur


def fusionAmelioree(T, deb, mil, fin):
    aux = T[deb:mil]
    i = 0 
    j = mil
    k = deb
    while i < len(aux) and j < fin:
        if aux[i] <= T[j]:
            T[k] = aux[i]
            i += 1
        else:
            T[k] = T[j]
            j += 1
        k += 1
    while i < len(aux):
        T[k] = aux[i]
        i += 1
        k += 1
    return T

def triFusionAmeliore(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)  
    if fin - deb <= 1:
        return T
    
    mil = (deb + fin) // 2
    
    triFusionAmeliore(T, deb, mil)
    triFusionAmeliore(T, mil, fin)
    
    fusionAmelioree(T, deb, mil, fin)
    
    return T

def trouveVainqueur(L):
    max = 0
    win = 0
    T = triFusionAmeliore(L)
    for i in range(1,len(T)):
        cur = 0
        if T[i-1] == T[i]:
            curr += 1
            

a = [1,1,3,3,3,3,3,3,3,3,1,2,2,3,5,6,4,8,7,9,5,6]
print(chercheVainqueur(a))