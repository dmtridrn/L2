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
    # À COMPLÉTER !
    return Vide

################
# Exercice 4.2

def statsHauteursABRparInsPuisSup(n, m) :
    ''' renvoie le tableau des hauteurs de m arbres de taille n,
    construits par genererABRparInsPuisSup '''
    # À COMPLÉTER !
    return []
###################################################################
#### Commentez ici les la hauteur des arbres en fonctions de n ####
###################################################################
# commentaires...
###################################################################


################
# Exercice 4.3

def genererABRparInsEtSup(permins, permsup) :
    ''' renvoie un couple (ABR, taille) construit par
    insertions/supressions successives entremêlées des éléments de
    permins et permsup respectivement '''
    # À COMPLÉTER !
    return Vide, 0


################
# Exercice 4.4

def statsHauteursABRparInsEtSup(n, m) :
    ''' renvoie le tableau des (taille, hauteur)s de m arbres
    construits par genererABRparInsEtSup sur 2 permutations de taille 2n
    '''
    # À COMPLÉTER !
    return []

###################################################################
#### Commentez ici les la hauteur des arbres en fonctions de n ####
###################################################################
# commentaires...
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
