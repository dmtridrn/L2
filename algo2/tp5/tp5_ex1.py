#!/usr/bin/env python3

from arbre import Vide, Noeud, Feuille, etiquetteRacine, estVide, filsGauche, filsDroit
from arbre import arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre10ABR1, arbre10ABR2, arbre100ABR1, arbre100ABR2, arbre100notABR, dessineArbreBinaire
from arbre import arbreBinaireVersFichier, arbreBinaireDeFichier
from ea4lib import printcol

######################
# Exercice 1.1 
#
def parcoursInfixe(arbre):
    res = []
    if arbre != None:
       res += parcoursInfixe(filsGauche(arbre))
       res += [etiquetteRacine(arbre)]
       res += parcoursInfixe(filsDroit(arbre))
    return []


######################
# Exercice 1.2

def estUnABR(arbre) :
    ''' test si un arbre binaire est un ABR '''
    # À COMPLÉTER !
    return False


######################
# Exercice 1.3

def minimumABR(arbre) :
    ''' l'étiquette minimale de l'arbre (en supposant que c'est un ABR).
    Renvoie None si l'arbre est vide '''
    # À COMPLÉTER !
    return None

def maximumABR(arbre) :
    ''' l'étiquette maximale de l'arbre (en supposant que c'est un ABR).
    Renvoie None si l'arbre est vide '''
    # À COMPLÉTER !
    return None


######################
# Exercice 1.4

def rechercheABR(arbre, elt) :
    ''' retourne True si elt est dans arbre (en supposant que arbre est un ABR) '''
    # À COMPLÉTER !
    return False

######################
# Exercice 1.5 

def insertionABR(arbre, elt) :
    ''' insère correctement elt dans arbre (en supposant que arbre est un ABR) '''
    # À COMPLÉTER !
    return Vide

#######################
# Exercice 1.6

def testInsertionPersonnel():
  # A REMPLIR
  return None

def testInsertion2():
  ''' Effectue des insertions successives, affiche le resultat dans dessin_ex1/monarbre.pdf, 
  et le compare avec le résultat attendu contenu dans arbre_insertion.txt'''
  elements=[7,3,9,65,12,1,5,8,13]
  arbre = Vide
  for elt in elements:
    arbre = insertionABR(arbre, elt)
  dessineArbreBinaire(arbre,"dessins_ex1/monarbre") # Dessine l'arbre dans le fichier dessins_ex1/monabre.pdf
  res = arbreBinaireDeFichier("tests/arbre_insertions.txt")
  print("Test insertions successives a partir d'un arbre vide:", end='')
  if arbre == res :
      printcol(" {ok}", "green")
  else:
      printcol(" {echec}", "red", end='')
      print(": obtenu ", arbre, end='')
      print(" <> attendu ", res)


#####################################################################
##  TESTS
#####################################################################


def testEstABR():
  print('Test estUnABR:')

  arbreNot = Noeud(7,Feuille(4),Noeud(10,Feuille(6),Feuille(12)))

  tests=[(arbreNot, False), (arbre3ABR1,True), (arbre3ABR2,True), (arbre3ABR3,True), (arbre10ABR1, True), (arbre10ABR2, True), (arbre100ABR1, True), (arbre100ABR2, True),(arbre100notABR, False)]
  for i, (a, val) in enumerate(tests):
    print (' - test %d/%d: ' % (i + 1, len(tests)), end='')
    res = estUnABR(a)
    if res != val:
      printcol(" {echec}", "red", end='')
      print(": obtenu ", res, end='')
      print(" <> attendu ", val)
    else:
      printcol(" {ok}", "green")

def testData():
  return  [Vide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre10ABR2, arbre100ABR1, arbre100ABR2]

def testResults():
    return [[minimumABR, 0,[None, 1, 1, 1, 1, 1, 1]],
        [maximumABR, 0, [None, 3, 3, 3, 10, 100, 100]],
        [rechercheABR, 1, [1,27,3,57,4,100,200],[False,False,True,False,True, True,False]]
        ]

def testAll() :
  tst = testResults()
  arbres = testData()
  print('Arbres : ')
  for j in range(len(arbres)) :
    print('- dessins_ex1/arb_' + str(j+1) + '.pdf')
    dessineArbreBinaire(arbres[j],'./dessins_ex1/arb_'+str(j+1))

  for i in range(len(tst)) :
    fname = tst[i][0]
    farg = tst[i][1]
    fres = tst[i][2 + farg]
    score = 0
    print('Test %s:' % fname.__name__)
    for j in range(len(arbres)) :
      a = arbres[j]
      print (' - test %d/%d: ' % (j + 1, len(arbres)), end='')
      res = fres[j]
      if (farg == 0) :
        res = fname(a)
      elif (farg == 1) :
        res = fname(a,tst[i][2][j])
      if (res == fres[j]) :
        printcol(" {ok}", "green")
        score += 1
      else :
        printcol(" {echec}", "red", end='')
        print(": obtenu ", res, end='')
        print(" <> attendu ", fres[j])
    printcol ('  score {%d/%d} ' % (score, len(arbres)), "cyan")

arbres = [Vide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre100ABR1, arbre100ABR2]
elements = [4,4,2,10,27,123]

def testInsertion():
  arbres = [Vide, arbre3ABR1, arbre3ABR2, arbre3ABR3, arbre100ABR1, arbre100ABR2]
  elements = [4,4,2,10,27,123]
  score = 0
  print('Test Insertion')
  for i in range(len(arbres)):
    print (' - test %d/%d: ' % (i + 1, len(arbres)), end='')
    a = arbreBinaireDeFichier('tests/insertion_%d.txt' % i)
    b = insertionABR(arbres[i],elements[i])
    if a == b :
      printcol(" {ok}", "green")
      score += 1
    else:
        printcol(" {echec}", "red", end='')
        print(": obtenu ", b, end='')
        print(" <> attendu ", a)
  printcol ('  score {%d/%d} ' % (score, len(arbres)), "cyan")

if __name__ == '__main__':
  testEstABR()
  testAll()
  testInsertion()
  testInsertion2()
  testInsertionPersonnel()
