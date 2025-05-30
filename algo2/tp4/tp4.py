#!/usr/bin/env python3

from tp3 import *
from random import randint

############################################################
# Exercice 1.1
#
# Tri rapide avec mémoire auxiliaire et en place
#

def triRapideNaif(T, alea=False):
    if len(T) <= 1:
        return T

    if(alea):
        r = randint(0, len(T) - 1)
    else:
        r = 0
    pivot = T[r]
    gauche = [x for x in T if x < pivot]
    milieu = [x for x in T if x == pivot]
    droite = [x for x in T if x > pivot]
    
    # Récursion et combinaison
    return triRapideNaif(gauche, alea) + milieu + triRapideNaif(droite, alea)

def triRapideEnPlace(T, debut=0, fin=None, alea=False) :
    if fin is None:
        fin = len(T)
    if fin - debut <= 1:
        return T
    if alea:
        r = randint(debut, fin - 1)
        T[debut], T[r] = T[r], T[debut]
    pivot = T[debut]
    i = debut
    for j in range(debut + 1, fin):
        if T[j] < pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[debut], T[i] = T[i], T[debut]
    triRapideEnPlace(T, debut, i, alea) 
    triRapideEnPlace(T, i + 1, fin, alea)
    return T

############################################################
# Exercice 1.2
#
# Tri rapide avec mémoire auxiliaire et en place avec pivot
# aléatoire : modifier les deux fonctions précédentes
#

def triRapideRandomise(T) :
    return triRapideNaif(T, alea=True)

def triRapideEnPlaceRandomise(T) :
    return triRapideEnPlace(T, debut=0, fin=len(T), alea=True)


############################################################
# Exercice 2.1
#
# les tableaux de taille < 15 sont triés par insertion, le
# reste avec l'algo de tri rapide usuel (randomisé bien sûr)
#

def triRapideAmeliore(T):
    if len(T)<15:
        T=triInsertionParLaDroite(T)
    else:
        T=triRapideEnPlaceRandomise(T)
    return T

############################################################
# Exercice 2.2
#
# Tri rapide (randomisé) seulement pour les tableaux de taille 
# >= 15 et ne fait rien pour les tableaux de taille < 15
#

def triRapidePartiel(T) :
    if len(T)<15:
        return T
    else:
        return triRapideEnPlaceRandomise(T)

############################################################
# Exercice 2.3
#
# Trie par insertion le résultat de triRapidePartiel(T).
#

def triSedgewick(T) :
    return triInsertionParLaDroite(triRapideAmeliore(T))


############################################################
# Exercice 3.1
#
# Fusionne les tranches T[deb:mil] et T[mil:fin] "presque en 
# place", c'est-à-dire en utilisant comme seule mémoire auxiliaire une
# copie de T[deb:mil], puis en réalisant la fusion directement dans
# T[deb:fin]

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


############################################################
# Exercice 3.2
#
# Générateur retournant, à chaque appel, les bornes de la
# monotonie suivante de T (sous-tableau de longueur maximale)

def monotonies(T) :
    deb = fin = 0
    while fin < len(T) :
        deb = fin
        fin = deb + 1
        
        if fin < len(T):
            if T[deb] <= T[fin]: #monotonie croissante
                while fin < len(T) and T[fin-1] <= T[fin]:
                    fin += 1
            else: #décroissante
                while fin < len(T) and T[fin-1] >= T[fin]:
                    fin += 1
        yield deb, fin


############################################################
# Exercice 3.3
#
# Initialise une **file** avec les (bornes des) monotonies de T, 
# puis tant que la file contient au moins 2 éléments :
# - si la monotonie en tête de file correspond à la fin de T, 
#   l'extrait et la replace en fin de file,
# - sinon, extrait et fusionne deux monotonies et replace le 
#   résultat dans la file.

def triFusionNaturel(T) :
    file = [ m for m in monotonies(T) ]
    
    # Tant qu'il reste au moins 2 éléments dans la file
    while len(file) >= 2:
        # Extraire la première monotonie
        (deb1, fin1) = file.pop(0)
        
        # Si cette monotonie correspond à la fin du tableau
        if fin1 == len(T):
            # La replacer à la fin de la file
            file.append((deb1, fin1))
            continue
        
        # Sinon, extraire la deuxième monotonie
        (deb2, fin2) = file.pop(0)
        
        # Fusionner les deux monotonies
        fusionAmelioree(T, deb1, fin1, fin2)
        
        # Replacer le résultat dans la file
        file.append((deb1, fin2))
    
    return T

############################################################
# Exercice 3.4 (tri à la manière de TimSort)
#
# Remplit une pile de monotonies de T en maintenant la condition de pile
# suivante : si m1 est la monotonie en sommet de pile, et m2 juste en
# dessous, alors len(m2) >= 2*len(m1)
# Pour maintenir cette condition, il peut être nécessaire de fusionner
# les deux monotonies en sommet de pile (et éventuellement de
# recommencer).
# Une fois toutes les monotonies empilées, les dépiler deux à deux,
# les fusionner, et réempiler le résultat

def triFaconTimSort(T) :
    monos = monotonies(T)
    premiere = next(monos)
    pile = [premiere]
    
    # Phase 1: Empiler les monotonies en maintenant la condition de pile
    for m in monos:
        pile.append(m)
        # Maintenir la condition de pile: len(m2) >= 2*len(m1)
        while len(pile) >= 2:
            m1 = pile[-1]  # Monotonie au sommet
            m2 = pile[-2]  # Monotonie juste en-dessous
            
            # Calculer les longueurs des monotonies
            len_m1 = m1[1] - m1[0]
            len_m2 = m2[1] - m2[0]
            
            # Si la condition n'est pas respectée, fusionner
            if len_m2 < 2 * len_m1:
                # Retirer les deux monotonies de la pile
                pile.pop()  # Retirer m1
                pile.pop()  # Retirer m2
                
                # Fusionner m2 et m1
                fusionAmelioree(T, m2[0], m1[0], m1[1])
                
                # Ajouter la monotonie fusionnée à la pile
                pile.append((m2[0], m1[1]))
            else:
                # La condition est respectée, on arrête les fusions
                break
    
    # Phase 2: Fusionner toutes les monotonies restantes dans la pile
    while len(pile) > 1:
        m1 = pile.pop()  # Retirer la monotonie du sommet
        m2 = pile.pop()  # Retirer la monotonie suivante
        
        # Fusionner m2 et m1 (en s'assurant du bon ordre)
        if m2[0] < m1[0]:
            fusionAmelioree(T, m2[0], m1[0], m1[1])
            pile.append((m2[0], m1[1]))
        else:
            fusionAmelioree(T, m1[0], m2[0], m2[1])
            pile.append((m1[0], m2[1]))
    
    return T


##############################################################
#
# Main
#

if __name__ == '__main__' :
    trisLents = [ triSelection ]
    trisInsertion = [triInsertionParLaDroite]
    trisRapides = [ triRapideNaif, triRapideEnPlace, triRapideRandomise, triRapideEnPlaceRandomise ]
    trisRapidesHybrides = [ triRapideAmeliore, triSedgewick ]
    trisFusions = [ triFusion, triFusionAmeliore ] 
    trisFusionsHybrides = [ triFusionNaturel, triFaconTimSort ]

    sys.setrecursionlimit(10000)

# Exercice 1

    #print("Exercice 1")
    #algos = trisRapides + [ triFusion ]
    #compareAlgos(algos)
    #algos = trisInsertion + [ triFusion, triRapideEnPlace]
    #compareAlgosSurTableauxTries (algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # pour randomPerm:
    # tous les tris rapides ont a peu près les mêmes performances, sans schéma qui se 
    # répète sur plusieurs fois le meme test (meme si le tri en place sans random parait généralement 
    # être le plus rapide)
    # pour randomTab:
    # le tri rapide en place parait toujours etre le plus performant, les deux tris les plus lents étant 
    # triFusion et triRapiderandomise avec un temps d'éxécution de 0.03 pour des tab de taille 100
    # contre 0.015 pour le triRapideEnPlace

    # de grosses différences commencent à se voir avec derangeUnPeu rev = true:
    # les deux plus lents: le triRapideNaif prend 0.02 seconde et le triRapideEnPlace prend 0.01 seconde
    # les trois autres tris avoisinnent les 0.002 seconde, ils sont donc bien plus efficaces
    #pour dérange un peu rev = false, le triRapideNaif reste de loin le plus lent avec 0.025
    #les autres tris gardent a peu de choses près le meme temps d'éxécution

    #pour dérangeunpeu rev = false avec tableaux énormes:
    #le triInsertionParLaGauche ne termine pas(j'ai arreté le programme après 5 minutes), ce qui s'explique facilement
    #par le fait que sa compléxité s'approche du pire cas possible pour ce genre de tab presque trié
    #pour les 3 autres tris, le triRapideEnPlace prend énormément de temps(2.5) contrairement aux deux autres 
    # qui sont optimisés pour ce genre de tab(0.03)
    ###################################################################

# Exercice 2

    #print("Exercice 2")
    #algos = trisRapidesHybrides + [ triRapideRandomise, triFusion ]
    #compareAlgos(algos, taille=2000, pas=200)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # pour randomPerm:
    # le trirapideamélioré est le plus rapide (0.005), suivi par le trifusion et le triSedgewick (0.006)
    # le plus lent est le triRapide randomisé (0.008) bien que les différences soient moindres

    #pour randomTab, les différences sont toujours moindres mais le triRapideAmeliore est le plus lent (0.006) 
    # comparé aux autres (0.005). L'ordre de rapidité change au fil des tests, expliqué par les différences proches de 0

    #pour derangeUnPeu rev = true:
    #les différences sont encore moins marquées, ont peut dire que les 4 tris sont équivalents (0.004)

    #pour rev = false on observe les mêmes comportements
    ###################################################################

# Exercice 3

    print("Exercice 3")
    algos = trisFusionsHybrides + [ triRapideRandomise, triFusion ]
    compareAlgos(algos, taille=2000, pas=200)
    algos = [ triFusionNaturel, triFaconTimSort, triShell ]
    compareAlgosSurTableauxTries(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # pour randomPerm: les tris semblent équivalents, le plus rapide étant le triFusionnaturel(0.004 comparé aux autres: 0.005)
    #pour randomTab, le trifusion naturel est le plus lent pour des petites tableaux
    #mais le triRapideRandomise est le plus lent pour les tailles max(0.006). le trifusion naturel rejoint les deux autres
    #pour les tableaux de grande taille (0.005)

    #de grandes différences commencent enfin à se faire voir pour dérangeunpeu rev = true:
    #plutot logiquement, les trifusionnaturel et trifaconTimSort sont lesp lus rapide (0.002) comparé aux deux autres (0.005 ou 0.006)
    # pour rev = false, le tri facon timsort est le plus rapide (0.002) suivi de près par le triFusionNaturel
    # les deux autres sont équivalents (0.004)

    #pour les très grands tableaux, le tri timsort est le plus rapide (0.018), suivi du trifusionnaturel (0.02)
    #le tri shell est dernier mais reste proche (0.023).

    #nous pouvons conclure en disant que, sur des petits tableaux, les algorithmes simples peuvent parfois être meilleurs
    # mais les algorithmes optimisés pour certains cas (par exemple dérange un peu qui contient énormément de monotonies) 
    # peuvent etre jusqu'à deux fois plus rapide.
    ###################################################################

