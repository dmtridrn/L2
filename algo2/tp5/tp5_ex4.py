#!/usr/bin/env python3

#importe indirectement tp5 et tp5_ex* pour * < 3
from tp5_ex3 import *
from math import sqrt

################
# Exercice 4.1

def genererABRparInsPuisSup(perm) :
    ''' renvoie un ABR de taille n construit par insertions successives
    des éléments de la permutation perm (de taille n^2), puis suppression
    d'éléments aléatoires '''
    from random import randint, choice
    from math import sqrt
    
    arbre = Vide
    for elt in perm:
        arbre = insertionABR(arbre, elt)
    
    n2 = len(perm)
    n = int(sqrt(n2))
    nb_suppressions = n2 - n
    
    elements = parcoursInfixe(arbre)
    
    for _ in range(nb_suppressions):
        index = randint(0, len(elements)-1)
        elt_a_supprimer = elements.pop(index)
        
        utiliser_predecesseur = (randint(0, 1) == 1)
        
        arbre = suppressionABR(arbre, elt_a_supprimer, utiliser_predecesseur)
    
    return arbre

################
# Exercice 4.2

def statsHauteursABRparInsPuisSup(n, m):
    ''' renvoie le tableau des hauteurs de m arbres de taille n,
    construits par genererABRparInsPuisSup '''
    from random import randint
    
    hauteurs = []
    for i in range(m):
        # Générer une permutation aléatoire de taille n²
        perm = permutation(n*n)
        
        # Construire l'ABR par insertion puis suppression
        arbre = genererABRparInsPuisSup(perm)
        
        # Calculer la hauteur et l'ajouter à la liste
        h = hauteur(arbre)
        hauteurs.append(h)
        
    return hauteurs
###################################################################
#### Commentez ici les la hauteur des arbres en fonctions de n ####
###################################################################
# la courbe des moyennes suit la courbe de log(n) normalisée mais nous pouvons
# observer que les pires cas se produisent moins qu'avec la méthode de l'exo 2
###################################################################


################
# Exercice 4.3

def genererABRparInsEtSup(permins, permsup) :
    ''' renvoie un couple (ABR, taille) construit par
    insertions/supressions successives entremêlées des éléments de
    permins et permsup respectivement '''
    from random import randint
    
    # Initialisation
    arbre = Vide
    taille = 0
    i, j = 0, 0  # Indices pour parcourir permins et permsup
    
    # Parcourir les deux permutations en alternant aléatoirement
    while i < len(permins) or j < len(permsup):
        # Choisir aléatoirement entre insertion et suppression
        # Si une des permutations est épuisée, on force l'autre opération
        if j >= len(permsup):
            choix = 0  # Insertion forcée
        elif i >= len(permins):
            choix = 1  # Suppression forcée
        else:
            choix = randint(0, 1)  # 0 pour insertion, 1 pour suppression
        
        if choix == 0 and i < len(permins):
            # Insertion d'un élément de permins
            arbre = insertionABR(arbre, permins[i])
            i += 1
            taille += 1
        elif choix == 1 and j < len(permsup):
            # Suppression d'un élément de permsup
            element = permsup[j]
            j += 1
            
            # Vérifier si l'élément est présent dans l'arbre
            elements = parcoursInfixe(arbre)
            if element in elements:
                # Choisir aléatoirement entre prédécesseur et successeur
                utiliser_predecesseur = (randint(0, 1) == 1)
                arbre = suppressionABR(arbre, element, utiliser_predecesseur)
                taille -= 1
    
    return arbre, taille


################
# Exercice 4.4

def statsHauteursABRparInsEtSup(n, m) :
    ''' renvoie le tableau des (taille, hauteur)s de m arbres
    construits par genererABRparInsEtSup sur 2 permutations de taille 2n
    '''
    from random import randint
    
    resultats = []
    for i in range(m):
        # Générer deux permutations aléatoires de taille 2n
        permins = permutation(2*n)
        permsup = permutation(2*n)
        
        # Construire l'ABR par insertion et suppression entremêlées
        arbre, taille = genererABRparInsEtSup(permins, permsup)
        
        # Calculer la hauteur et ajouter le couple (taille, hauteur)
        h = hauteur(arbre)
        resultats.append((taille, h))
    
    return resultats

###################################################################
#### Commentez ici les la hauteur des arbres en fonctions de n ####
###################################################################
# les points suivent globalement la forme de la courbe logarithmique mais sont pour la plupart très au dessus
# Cela indique que la croissance de la hauteur reste logarithmique mais que le facteur multiplicatif
# est bien plus élevé que pour un ABR idéal.
###################################################################

####### NE PAS MODIFIER #######

def tracerInsPuisSup(limite, pas, m):
    print('Test InsPuisSup')
    lx, ly, ly_moy = [], [], []
    for i in range(1, limite, pas) :
        print('Stat calculée : %d / %d' % (i, limite), end="\r")
        tmp = statsHauteursABRparInsPuisSup(i, m)
        lx.extend([i]*m)
        ly.extend(tmp)
        ly_moy.append(sum(tmp)/m)
    print('Stat calculée : %d / %d' % (limite, limite))
    plt.plot([((math.log(i,2)  * ly_moy[-1]) / math.log(limite-1,2) if i>0 else 0) for i in range(limite)], color="blue", label="log(n) normalisé")
    plt.plot(lx, ly, '.', color="orange", label = "hauteurs observées")
    plt.plot(range(1,limite,pas), ly_moy, color="red", label="moyenne des hauteurs")
    plt.ylabel('hauteur')
    plt.xlabel('n = nombre noeuds')
    plt.title('Distribution des hauteurs d\'arbres aléatoires obtenus par insertions puis suppressions')
    plt.show()
    print('')

def tracerInsEtSup(limite, pas, m):
    print('Test InsEtSup')
    lx, ly = [], []
    plt.plot([(math.log(i,2) if i>0 else 0) for i in range(limite)], color="blue", label='log(n) non normalisé')
    for i in range(1, limite, pas) :
        print('Stat calculée : %d / %d' % (i, limite), end="\r")
        tailles, hauteurs = list(zip(*statsHauteursABRparInsEtSup(i, m)))
        lx.extend(tailles)
        ly.extend(hauteurs)
    print('Stat calculée : %d / %d' % (limite, limite))
    plt.plot(lx, ly, '.', color="green", label = "hauteurs et tailles observées")
    plt.ylabel('hauteur(n)')
    plt.xlabel('n = nombre noeuds')
    plt.title('Distribution des hauteurs d\'arbres aléatoires obtenus par insertions et suppressions')
    plt.show()
    print('')


if __name__ == '__main__':
    tracerInsPuisSup(80,5,5)
    tracerInsEtSup(800,50,10)
