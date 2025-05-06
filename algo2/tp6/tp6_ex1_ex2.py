#!/usr/bin/env python3

from random import randint
from time import process_time
import matplotlib.pyplot as plt
import math
# Pour l'affichage des résultats
from ea4lib import printcol

MARQUE = (None, None)
A = (math.sqrt(5)-1)/2

class TableHachage:
    # constructeur
    # par défaut, la fonction h est initialisée à la fonction hash de python 
    # qui renvoie le haché de n'importe quel objet python passé en paramètre.
    def __init__(self, lg=8, h=hash, h1=None, h2=None,  tmin=0.25, tmax=0.75):
        if h1 == None or h2 == None:
            raise ValueError('une table doit avoir une fonction de hachage.')
        self.cles = [None]*lg
        self.lg = lg 
        self.nbCles = 0
        self.nbMarques = 0
        self.h = h
        self.h1 = h1
        self.h2 = h2
        self.tmin = tmin
        self.tmax = tmax       

    # renvoie True si la ième case est vide, False sinon
    def estVide(self, i):
        return self.cles[i] == None

    # renvoie True si la ième case est marquée, False sinon
    def estMarquee(self, i):
        return self.cles[i] == MARQUE
    
    # renvoie la ième clé si elle existe et lève une exception sinon
    def getCle(self, i):
        if self.estVide(i) or self.estMarquee(i): raise ValueError('pas de clé!')
        return self.cles[i][1]

    # renvoie le haché (stocké) de la ième clé si il y a une clé et lève une exception sinon
    def getHash(self, i):
        if self.estVide(i) or self.estMarquee(i): raise ValueError('pas de clé!')
        return self.cles[i][0]

    # génère les positions successives de sondage pour la clé cle
    def positionsSuccessives(self, cle):
        hcle = self.h(cle)
        ind = self.h1(hcle, self.lg) % self.lg
        pas = self.h2(hcle, self.lg)
        for i in range(self.lg):
            yield ind
            ind = (ind+pas) % self.lg
		
    def __str__(self) :
        return str((self.cles, self.lg, self.nbCles, self.nbMarques, self.tmin, self.tmax))


##############################################################
#
# fonctions de hachage
#

def hash1(hcle, taille):
    pos = hcle % taille
    return pos;

def hash2(hcle, taille):
    return 1;

def hash1b(hcle, taille):
    
    return

def hash2b(hcle, taille):
    #A COMPLETER
    return


##############################################################
#
# fonctions de recherche et modifications dans une table de hachage
#


def rechercher(table, cle, flag=False):
    hcle = table.h(cle)
    
    pos_insertion = None
    
    for pos in table.positionsSuccessives(cle):
        if table.estVide(pos):
            if pos_insertion is None:
                pos_insertion = pos
            break
        
        if table.estMarquee(pos):
            if pos_insertion is None:
                pos_insertion = pos
            continue
        
        if table.getHash(pos) == hcle:
            if table.getCle(pos) == cle:
                return pos   
    if flag:
        return pos_insertion
    else:
        return None 
    

def inserer(table, cle):
    pos = rechercher(table, cle, True)
    if not table.estVide(pos) and not table.estMarquee(pos):
        if table.getCle(pos) == cle:
            return table
    hcle = table.h(cle)
    if table.estVide(pos):
        table.cles[pos] = (hcle, cle)
        table.nbCles += 1
    elif table.estMarquee(pos):
        table.cles[pos] = (hcle, cle)
        table.nbCles += 1
        table.nbMarquees -= 1
    return table

def supprimer(table, cle):
    #A COMPLETER
    return table

def redimensionner(table, l):
    #A COMPLETER
    return table

##############################################################
#
# Mesures
#

def random_liste(taille, maxi):
    L = []
    S = set()
    for i in range(taille):
        r = randint(0, maxi)
        while r in S:
            r = randint(0, maxi)
        S.add(r)
        L.append(r)
    return L

def liste_collisions(taille, ite):
    L = [1]
    for i in range(10):
        pas = (i+ite)*taille
        L += [j+pas for j in range(taille//10)]
    return L

def liste_paquets(taille, maxi):
    L = []
    S = set()
    i = 0
    while i < taille :
        r = randint(0, maxi)
        while r in S:
            r = randint(0, maxi)
        S.add(r)
        L.append(r)
        i += 1
        if i == taille: break
        for j in range(maxi//200):
            x = r+randint(0, maxi//200)-maxi//400
            if not x in S:
                S.add(x)
                L.append(x)
                i += 1
                if i == taille: break
        
    return L

def taille_max_cluster(table):
    maxi = 0
    max_tmp = 0
    for i in range(table.lg):
        if table.estVide(i):
            maxi = max_tmp if max_tmp > maxi else maxi
            max_tmp = 0
        else:
            max_tmp += 1
    return maxi

def stats(h, h1, h2, taille_max, tmin, tmax, alea=False, rep=1, pas=10, redim=False):
    t_crea = [None] * (taille_max//pas)
    clust = [None] * (taille_max//pas)
    t_rech = [None] * (taille_max//pas)

    for i in range(0,taille_max,pas):
        cluster = 0
        tps = 0
        max_cl = 0
        tr = 0
        for j in range(rep):
            if alea: L = random_liste(i+1, 100000)
            else: L = liste_paquets(i+1, 100000)
            if redim: table = TableHachage(64, h, h1, h2, tmin, tmax)
            else:
                lg = 2**math.ceil(math.log((i+1)/tmax,2))
                table = TableHachage(lg , h, h1, h2, tmin, tmax)
            for cle in L:
                deb = process_time()
                table = inserer(table, cle)
                tps += process_time() - deb
            cluster += taille_max_cluster(table)
            tr += test_recherche(table, L)
        t_crea[i//pas] = tps/rep
        clust[i//pas] = cluster/rep
        t_rech[i//pas] = tr/rep
    return t_crea, clust, t_rech

def test_recherche(table, L):
    tps = 0
    for cle in L: 
        deb = process_time()
        rechercher(table, cle)
        tps += process_time() - deb
    return tps/len(L)
    
##############################################################
#
# Courbes
#

def mesure(algo, T) :
    debut = process_time()
    algo(T)
    return process_time() - debut

couleurs = ['b', 'g', 'r', 'm', 'c', 'k', 'y']


def courbes(liste_h, taille_max, tmin, tmax, alea=False, styleLigne='-', rep=1, pas=10, redim=False):
    x = [i for i in range(0,taille_max,pas)]
    s = [None] * len(liste_h)
    for i, (h, h1, h2) in enumerate(liste_h):
        s[i] = stats(h, h1, h2, taille_max, tmin, tmax, alea, rep, pas, redim)
    for i in range(len(s)):
        tps = s[i][0]
        plt.plot(x, tps, color=couleurs[i%len(couleurs)], linestyle=styleLigne, label=liste_h[i][1].__name__+", "+liste_h[i][2].__name__)        
    affiche("tps d'exec moyen pour céer une table par insertions successives")
    for i in range(len(s)):
        clust = s[i][1]
        plt.plot(x, clust, color=couleurs[i%len(couleurs)], linestyle=styleLigne, label=liste_h[i][1].__name__+", "+liste_h[i][2].__name__)
    affiche("taille moyenne du cluster max")
    for i in range(len(s)):
        clust = s[i][2] 
        plt.plot(x, clust, color=couleurs[i%len(couleurs)], linestyle=styleLigne, label=liste_h[i][1].__name__+", "+liste_h[i][2].__name__)
    affiche("temps d'execution moyen pour une recherche reussie")

def affiche(label) :
  plt.xlabel('taille du tableau')
  plt.ylabel(label)
  plt.legend(loc='upper left')
  plt.show()
  
##############################################################
#
# Main
#
if __name__ == '__main__':
    L = [13, 15, 70, 28, 18, 7, 20, 6, 5, 8, 32, 4, 38]
    printcol("{création de la table}", 'bold')
    table = TableHachage(32, hash, hash1, hash2, 0.25, 0.5)
    
    for cle in L:
        table = inserer(table, cle)
    
    print("  liste de cles :",L)
    if table != None :
        print("  table de hachage :", table.cles)
        print("  longueur de la table :", table.lg)

    trouve = True
    for cle in L:
        if(rechercher(table, cle)) == None:
            printcol("{  Il y a un problème : }", 'red', end='')
            print("cle ", cle, " non trouvée")
            trouve = False
    
    if trouve:
        printcol("{insertions et recherches réussies. Bravo !}", 'green')
    else:
        printcol("{echec des insertions et recherches}", 'red')
    print()

    printcol("{suppression de l'element 6:}", 'bold')
    if table != None :
        print("  ", supprimer(table, 6).cles)
        if rechercher(table, 6) == None :
            printcol("{suppression réussie. Bravo !}", 'green')
        else:
            printcol("{echec de la suppression}", 'red')
    print()
    
    printcol("{recherche de l'élément 38: }", 'bold')
    if rechercher(table, 38) != None :
         printcol("{recherche réussie. Bravo !}", 'green')
    else:
        printcol("{echec de la recherche. Attention hash1(6)%32 = hash1(38)%32}", 'red')
    print()
    
    printcol("{puis insertion de l'element 6:}", 'bold')
    if table != None :
        print("  ", inserer(supprimer(table, 6), 6).cles)
        if rechercher(table, 6) != None :
            printcol("{insertion de 6 réussie. Bravo !}", 'green')
        else:
            printcol("{echec de l'insertion}", 'red')
    print()
    
    printcol("{test redimensionnement avec ajouts de [19, 78, 234, 93]: }", 'bold')
    for cle in [19, 78, 234, 93]:
        table = inserer(table, cle)
    if table != None :
        if table.lg == 64 :
            printcol("{redimensionnement lors de l'insertion réussie. Bravo !}", 'green')
        else:
            printcol("{échec du redimensionnement lors de l'insertion}", 'red')
    else:
        print()
    print()
    
    printcol("{test redimensionnement avec suppressions de [15, 18]:} ", 'bold')
    for cle in [15, 18]:
        table = supprimer(table, cle)
    
    if table != None :
        if table.lg == 32 :
            printcol("{redimensionnement lors de la suppression réussie. Bravo !}", 'green')
        else:
            printcol("{échec du redimensionnement lors de la suppression}", 'red')
    print()  

    printcol("{test nettoyage des cases marquées avec suppressions de [70, 13, 20, 4, 32, 19, 7] puis insertions de [165, 265, 87, 94, 112, 53, 39]: }", 'bold')
    for el in [70, 13, 20, 4, 32, 19, 7]:
        table = supprimer(table, el)
    for el in [165, 265, 87, 94, 112, 53, 39]:
        table = inserer(table, el)

    if table != None :
        if table.lg == 32 and table.cles[0] == None:
            printcol("{nettoyage des cases marquées lors de l'insertion réussie. Bravo !}", 'green')
        else:
            printcol("{échec du nettoyage des cases marquées lors de l'insertion}", 'red')
    print()  

    
    
    tmin, tmax = 0.25, 0.75
    liste_hash = [[hash,hash1,hash2],[hash,hash1b, hash2], [hash,hash1, hash2b], [hash,hash1b, hash2b]]

    #Tests avec jusqu'à 2000 (par pas de 50) clés de valeurs proches par plages, avec taux tmin et tmax.
    #Pour chaque taille, on fait des tests sur rep=10 listes.
    #courbes(liste_hash, 2000, tmin, tmax, rep=10, pas=100)

    #Tests avec jusqu'a 2000 (par pas de 50) clés aléatoires, avec taux tmin et tmax.
    #Pour chaque taille, on fait des tests sur rep=10 listes.
    #courbes(liste_hash, 2000, tmin, tmax, alea=True, rep=10, pas=100)

    ########################################################################
    # vos commentaires en réponse à la question 6 de l'exercice 1...
    #
    ########################################################################

    liste_hash = [[hash,hash1b, hash2], [hash,hash1, hash2b], [hash,hash1b, hash2b]]

    #Tests avec jusqu'à 2000 (par pas de 50) clés de valeurs proches par plages, avec taux tmin et tmax.
    #Pour chaque taille, on fait des tests sur rep=10 listes.
    #courbes(liste_hash, 2000, tmin, tmax, rep=10, pas=100, redim=True)

    #Tests avec jusqu'a 2000 (par pas de 50) clés aléatoires, avec taux tmin et tmax.
    #Pour chaque taille, on fait des tests sur rep=10 listes.
    #courbes(liste_hash, 2000, tmin, tmax, alea=True, rep=10, pas=100, redim=True)

    ########################################################################
    # vos commentaires en réponse à la question 3 de l'exercice 2...
    #
    ########################################################################
