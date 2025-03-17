def fuisionIterative(t1, t2):
    a = 0
    b = 0
    res = []
    cpt = 0
    while a < len(t1) and b < len(t2):
        if t1[a] <= t2[b]:
            res.append(t1[a])
            a += 1
        else:
            res.append(t2[b])
            b += 1
            cpt += len(t1) - a
    
    while a < len(t1):
        res.append(t1[a])
        a += 1
    while b < len(t2):
        res.append(t2[b])
        b += 1
    
    return cpt, res


def nbInversionsNaive(t):
    res = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[j] < t[i]:
                res.append([t[j], t[i]])
    return len(res)

def nbInversions(T):
    if len(T) <= 1:
        return 0, T
        
    milieu = len(T) // 2
    gauche = T[:milieu]
    droite = T[milieu:]
        
    inv_gauche, gauche_triee = nbInversions(gauche)
    inv_droite, droite_triee = nbInversions(droite)
        
    inversions_croisees, tableau_trie = fuisionIterative(gauche_triee, droite_triee)

    total_inversions = inv_gauche + inv_droite + inversions_croisees

    return total_inversions, tableau_trie

a = [1,2,3,8,9]
b = [2,6,8,9,14]
c = a+b
print(nbInversionsNaive(c))
print(fuisionIterative(a,b))
print(nbInversions(c))
