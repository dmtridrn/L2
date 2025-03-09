#!/usr/bin/env python3

import sys

version = sys.version_info
if version.major < 3:
    sys.exit(
        "Python2 n'est PLUS supporté depuis le 1er Janvier 2020, merci d'installer Python3"
    )

from random import randint
from time import process_time as clock

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:
    sys.exit("Le module matplolib est nécessaire pour ce TP.")


############################################################
# Exercice 1.1
#
# Tri selection
#

def triSelection(T):
    n = len(T)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if T[j] < T[min]:
                min = j
        if min != i:
                T[i], T[min] = T[min], T[i]
    return T

############################################################
# Exercice 1.2
#
# randomPerm prend en paramètre un entier n et renvoie une
# permutation aléatoire de longueur n dont l'algorithme s'appuie
# sur le tri sélection
#

def randomPerm(n):
    T = [i + 1 for i in range(n)]
    for i in range(n-1):
        r = randint(i,n-1)
        if i != r:
            T[i], T[r] = T[r], T[i]
    return T

############################################################
# Exercice 1.3
#
# testeQueLaFonctionTrie prend en paramètre une fonction de
# tri f et l’applique sur des permutations aléatoires de
# taille i variant de 2 à 100 et vérifie que le résultat est
# un tableau trié
#

def testeQueLaFonctionTrie(f):
    for i in range(10):
        r = randint(2,100)
        t = randomPerm(r)
        tri = f(t)
        if testTabTrie(tri):
            print("Tri réussi")
        else:
            print(tri)
            print("Tri non réussi")
            return False
    return True

def testTabTrie(t):
    for i in range(1, len(t)):
        if t[i-1] >= t[i]:
            return False
    return True
        

############################################################
# Exercice 1.4
#
# randomTab prend des entiers n, a et b et renvoie un tableau
# aléatoire de taille n contenant des entiers compris entre
# les bornes a et b.
#

def randomTab(n, a, b):
    T = [0] * n
    for i in range(n):
        r = randint(a,b)
        T[i] = r
    return T


############################################################
# Exercice 1.5
#
# derangeUnPeu prend des entiers n, k et un booleen rev et
# effectue k échanges entre des positions aléatoires sur la
# liste des entiers de 1 à n si rev vaut False ou sur la
# liste des entiers n à 1 si rev vaut True.
#

def derangeUnPeu(n, k, rev):
    T = [n - i for i in range(n)] if rev else [i + 1 for i in range(n)]
    for i in range(k):
        r = randint(0,n-1)
        r2 = randint(0,n-1)
        T[r],T[r2] = T[r2],T[r]
    return T

############################################################
# Exercice 2.1
#
# Deux variantes du tri par insertion présentées dans le TD4.

def triInsertionParLaGauche(T):
    for i in range(len(T)):
        for j in range(i+1):
            if T[i] > T[j]:
                break
        for k in range(j,i):
            T[i],T[k]=T[k],T[i]
    return T

def triInsertionParLaDroite(T):
    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j-1] <= T[j]: 
                break
            T[j-1],T[j] = T[j],T[j-1]
    return T

############################################################
# Exercice 2.2
#
# Un tri fusion
#

def fusion(T1, T2):
    i,j=0,0
    res=[]
    while i<len(T1) and j<len(T2):
        if T1[i]<T2[j]:
            res.append(T1[i])
            i+=1
        else:
            res.append(T2[j])
            j+=1
    while i<len(T1):
        res.append(T1[i])
        i+=1
    while j<len(T2):
        res.append(T2[j])
        j+=1
    return res


def triFusion(T, debut=0, fin=None) :
    if fin is None:
        fin = len(T)
    if fin - debut < 2:
        return T[debut:fin]
    else:
        milieu = (debut + fin)//2
        gauche = triFusion(T, debut, milieu)
        droite = triFusion(T, milieu, fin)
    return fusion(gauche, droite)

############################################################
# Exercice 3.1
#
# Trie par insertion le sous-tableau T[debut::gap] de T
#

def triInsertionPartiel(T, gap, debut):
    for i in range(debut,len(T),gap):
        tmp=T[i]
        j=i-1
        while j>=0 and T[j]>tmp:
            T[j+1]=T[j]
            j=j-1
        T[j+1] = tmp
    return T


############################################################
# Exercice 3.2
#
# Tri Shell
#

def triShell(T):
    triInsertionPartiel(T,701,0)
    triInsertionPartiel(T,301,0)
    triInsertionPartiel(T,132,0)
    triInsertionPartiel(T,57,0)
    triInsertionPartiel(T,23,0)
    triInsertionPartiel(T,10,0)
    triInsertionPartiel(T,4,0)
    triInsertionPartiel(T,1,0)
    return T


##############################################################
#
# Mesure du temps
#


def mesure(algo, T):
    debut = clock()
    algo(T)
    return clock() - debut


def mesureMoyenne(algo, tableaux):
    return sum([mesure(algo, t[:]) for t in tableaux]) / len(tableaux)


couleurs = [
    "b",
    "g",
    "r",
    "m",
    "c",
    "k",
    "y",
    "#ff7f00",
    ".5",
    "#00ff7f",
    "#7f00ff",
    "#ff007f",
    "#7fff00",
    "#007fff",
]
marqueurs = [
    "o",
    "^",
    "s",
    "*",
    "+",
    "d",
    "x",
    "<",
    "h",
    ">",
    "1",
    "p",
    "2",
    "H",
    "3",
    "D",
    "4",
    "v",
]


def courbes(algos, tableaux, styleLigne="-"):
    x = [t[0] for t in tableaux]
    for i, algo in enumerate(algos):
        print("Mesures en cours pour %s..." % algo.__name__)
        y = [mesureMoyenne(algo, t[1]) for t in tableaux]
        plt.plot(
            x,
            y,
            color=couleurs[i % len(couleurs)],
            marker=marqueurs[i % len(marqueurs)],
            linestyle=styleLigne,
            label=algo.__name__,
        )


def affiche(titre):
    plt.xlabel("taille du tableau")
    plt.ylabel("temps d'execution")
    plt.legend(loc="upper left")
    plt.title(titre)
    plt.show()


def compareAlgos(algos, taille=1000, pas=100, ech=5):
    # taille = 1000 : taille maximale des tableaux à trier
    # pas = 100 : pas entre les tailles des tableaux à trier
    # ech = 5 : taille de l'échantillon pris pour faire la moyenne
    for tri in algos:
        if testeQueLaFonctionTrie(tri):
            print(tri.__name__ + ": OK")
        else:
            print(tri.__name__ + ": échoue")
    print()
    print("Comparaison à l'aide de randomPerm")
    tableaux = [[i, [randomPerm(i) for j in range(ech)]] for i in range(2, taille, pas)]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de randomPerm")
    print()

    print("Comparaison à l'aide de randomTab")
    tableaux = [
        [i, [randomTab(i, 0, 1000000) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de randomTab")
    print()

    print("Comparaison à l'aide de derangeUnPeu (rev = True)")
    tableaux = [
        [i, [derangeUnPeu(i, 10, True) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derangeUnPeu (rev = True)")
    print()

    print("Comparaison à l'aide de derangeUnPeu (rev = False)")
    tableaux = [
        [i, [derangeUnPeu(i, 10, False) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")
    print()


def compareAlgosSurTableauxTries(algos, taille=20000, pas=1000, ech=10):
    print("Comparaison à l'aide de derangeUnPeu (rev = False)")
    tableaux = [
        [i, [derangeUnPeu(i, 10, False) for j in range(ech)]]
        for i in range(2, taille, pas)
    ]
    courbes(algos, tableaux, styleLigne="-")
    affiche("Comparaison à l'aide de derangeUnPeu (rev = False)")


##############################################################
#
# Main
#

if __name__ == "__main__":
    trisInsertion = [triInsertionParLaGauche,triInsertionParLaDroite]
    trisLents = [triSelection]

    sys.setrecursionlimit(4000)

    # exercice1

    print("Exercice 1")
    #algos = [triSelection]
    #compareAlgos(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # on observe que le tri par sélection a un comportement similaire pour tous les types de tableau testés
    # il ne tire aucun avantage des tableaux légèrements altérés par derangeUnPeu()
    ###################################################################

    # exercice2

    print("Exercice 2")
    #algos += trisInsertion + [triFusion]
    #compareAlgos(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # sur des tableaux complètements aléatoires (randomperm), le trifusion est celui qui prend le moins de temps avec un temps d'éxécution de 0.002 voire 0.000 pour un tab[1000]
    # le triselection et le triinsertionparlagauche suivent une courbe similaire beaucoup plus lente que le trifusion d'éxécution de 0.08 pour un tab[1000]
    # mais le triionsertionparladroite est le plus lent avec un temps d'éxécution de 0.016 pour un tab[1000]

    # sur les tableaux un peu dérangés avec reev = true (reverse) les différences sont plus marquées:
    # on retrouve les memes 3 "groupes": le trifusion avec un temps d'éxécution de 0.000 pour un tab[1000]
    # le triselection et triinsertionparlagauche avec un temps d'éxécution de 0.008 pour un tab[1000]
    # et enfin le triinsertionparladroite avec un temps d'éxécution de 0.025 pour un tab[1000]*

    #on observe de gros changements pour rev = false sur les meme types de tableau:
    #on a le trifusion et le triinsertionparladroite avec un temps d'éxécution de 0.000 pour un tab[1000]
    #les deux autres ont une courbes montant beaucoup plus avec un temps d'éxécution de 0.012 pour un tab[1000]  
    ###################################################################

    # exercice3

    print("Exercice 3")
    #algos = [triShell]
    #compareAlgos(algos)

    #compare tous les algos

    #print("Comparaisons de tous les algos")
    #algos = trisInsertion + trisLents + [triFusion, triShell]
    #compareAlgos(algos, taille=2000, pas=200)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # on voit grace à la courbe que le trishell est le moins efficace pour les tableaux derangeunpeu rev = true
    # il est similaire en temps d'éxéécution aux triselection et tris par insertion pour les tableaux randomperm, seul le tri fusion se démarque par sa rapidité pour ce genre de tableau 
    # on observe les memes comportements avec les tableaux de la forme randomtab
    #le trishell est le deuxième plus lent pour les derange un peu rev = true, le trifusion reste le plus performant
    #d'un autre côté pour rev = false le tri shell est comparable au trifusion et est très très proche du tri insertion par la droite
    #le tri selection et l'autre tri insertion restent les moins performants sur ce type de tableau
    ###################################################################

    # compare les tris fusions et Shell

    print("Comparaisons des tris fusion et Shell")
    algos = [triFusion, triShell]
    #compareAlgos(algos, taille=10000, pas=500)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # pour les très grands tableaux de type randomperm, le tri shell prend énormément de temps (plus d'une seconde)
    # tandis que le tri fusion garde un temps d'éxécution quasi instantané
    # on observe le meme comportement pour random tab et derangeunpeu rev = true, le tri shell n'a pas l'air d'être adapté pour des tableau de cette taille
    #cependant, pour derangeunpeu rev = false, le tri shell est 2x plus rapide que le tri fusion 
    ###################################################################

    # comparaison sur tableaux presque triés

    # print("\nComparaisons sur tableaux presque triés")
    # algos = [triFusion, triShell]
    # compareAlgosSurTableauxTries(algos)

    ###################################################################
    ##### Commentez ici les résultats obtenus pour les différents #####
    ##### algorithmes sur les différents types de tableaux ############
    ###################################################################
    # on remarque que pour des tableaux très grands, le trishell est bien plus rapide que le tri fusion, avec un temps d'éxécution de 0.006
    # contre 0.2 pour le tri fusion
    ###################################################################


    #Exercice 4

    print("\nComparaison tri fusion et méthode sort\n")
def sortNormalise(T):
    T.sort()
    return T

# Générer une grande permutation aléatoire
n = 10**6  # 1 million d'éléments
print("Génération d'une permutation aléatoire de 10^6 éléments:")
t = randomPerm(n)

# Faire des copies pour les deux algorithmes
t_fusion = t.copy()
t_sort = t.copy()

# Mesurer les temps d'exécution
print("Mesure du temps pour le tri fusion:")
temps_fusion = mesure(triFusion, t_fusion)

print("Mesure du temps pour la méthode sort:")
temps_sort = mesure(sortNormalise, t_sort)

# Afficher les résultats
ratio = temps_fusion / temps_sort
print(f"\nTemps d'exécution du tri fusion: {temps_fusion:.6f} secondes")
print(f"Temps d'exécution de sort: {temps_sort:.6f} secondes")
print(f"Ratio tri fusion / sort: {ratio:.2f}")

    ###########################################################################
    ### Expliquez ici la difference de performance entre tri fusion et sort ###
    ###########################################################################
    # on observe un ratio trifusion/sort de 12.8 avec le sort faisant le tri en 0.156 secondes et le tri fusion en 2 secondes
    # après quelques recherches, ces différences s'expliquent de plusieurs manières:
    # le tri sort est écrit en C, réputé pour etre un des langages les plus rapides
    # La méthode sort utilise Timsort, un algorithme hybride optimisé écrit en C
    ###########################################################################
    
