def fuisionIterative(t1,t2):
    a = 0
    b = 0
    res = []
    cpt = 0
    while a<len(t1) and b<len(t2):
        if(t1[a] < t2[b] and a<len(t1)):
            res.append(t1[a])
            a+=1
        elif(t1[a] > t2[b] and b<len(t2)):
            res.append(t2[b])
            b+=1
            cpt+=len(t1) - a
        else:
            res.append(t1[a])
            a+=1
            res.append(t2[b])
            b+=1
            cpt+= len(t2) - b
    while a < len(t1):
        res.append(t1[a])
        a += 1
    while b < len(t2):
        res.append(t2[b])
        b += 1
    return cpt,res

def nbInversions(T):
    """Compte le nombre d'inversions dans T en temps Θ(n log n)"""
    # Cas de base
    if len(T) <= 1:
        return 0, T
    
    # Diviser
    milieu = len(T) // 2
    T1 = T[:milieu]
    T2 = T[milieu:]
    
    # Conquérir (résoudre récursivement)
    inv1, T1_trie = nbInversions(T1)  # inversions dans la première moitié
    inv2, T2_trie = nbInversions(T2)  # inversions dans la seconde moitié
    
    # Fusionner et compter les inversions entre les deux moitiés
    inv_trans, T_trie = fuisionIterative(T1_trie, T2_trie)
    
    # Combiner les résultats
    total_inversions = inv1 + inv2 + inv_trans
    
    return total_inversions, T_trie

def nbInversionsNaive(t):
    res = []
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[j] < t[i]:
                res.append([t[j], t[i]])
    return len(res)

a = [1,2,3,8,9,10]
b = [2,6,8,9,14]
c = a+b
print(nbInversionsNaive(c))
print(fuisionIterative(a,b))
print(nbInversions(c))
