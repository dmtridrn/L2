#!/usr/bin/env python3

#importe indirectement tp5, ea4lib et tp5_ex* pour * < 2
from tp5_ex2 import *

################
# Exercice 3.1

def supprimerPlusPetit(arbre) :
    ''' Supprime le plus petit élément de arbre. Renvoie la paire (elt,new_arbre)
    où elt est le plus petit élement de arbre et new_arbre est le nouvel arbre.
    Renvoie None et Vide quand arbre est vide.'''
    # À COMPLÉTER !
    return None, Vide


def supprimerPlusGrand(arbre) :
    ''' Supprime le plus grand élément de arbre. Renvoie la paire (elt,new_arbre)
    où elt est le plus grand élement de arbre et new_arbre est le nouvel arbre.
    Renvoie None et Vide quand arbre est vide.'''
    # À COMPLÉTER !
    return None, Vide

################
# Exercice 3.2

def suppressionABR(arbre, elt, pred=True) :
    ''' supprime le noeud d'étiquette elt dans l'arbre
    Pred vaut True si on priorise le prédécesseur, et False si on
    priorise le successeur'''
    # À COMPLÉTER !
    return None

#####################################################################
##  TESTS
#####################################################################

def testSuppression(pred):
  arbres = [arbre3ABR1, arbre3ABR1, arbre10ABR2, arbre10ABR2, arbre100ABR1, arbre100ABR1, arbre100ABR1, arbre100ABR1]
  elements = [1, 4, 3, 7, 55, 1, 49, 43]
  score = 0
  print('Test Suppression (pred = ' + str(pred) + ')')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    elt = elements[i]
    a = suppressionABR(arbres[i],elt,pred)
    if a == None : a = arbres[i]
    if pred : 
        res = arbreBinaireDeFichier('tests/testSuppression_%d.txt' % i)
    else :
        res = arbreBinaireDeFichier('tests/testSuppressionSucc_%d.txt' % i)
    if a == res :
      printcol(" {ok}", "green")
      score += 1
      #dessineArbreBinaire(a,'obtenu_'+str(i))
    else:
        printcol(" {echec}", "red", end='')
        #print(": obtenu ", a, end='')
        #print(" <> attendu ", res[i])
        dessineArbreBinaire(arbres[i], 'dessins_ex3/arbre_'+str(i+1))
        if pred :
            dessineArbreBinaire(a,'dessins_ex3/obtenuPred_'+str(i+1))
            dessineArbreBinaire(res, 'dessins_ex3/attenduPred_'+str(i+1))
        else :
            dessineArbreBinaire(a,'dessins_ex3/obtenuSuc_'+str(i+1))
            dessineArbreBinaire(res, 'dessins_ex3/attenduSuc_'+str(i+1))
        print("")
  printcol ('  score {%d/%d} ' % (score, len(arbres)), "cyan")
  score=0


if __name__ == '__main__':
    testSuppression(True)
    testSuppression(False)
