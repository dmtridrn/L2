#!/usr/bin/env python3

import tp6_ex1_ex2

def mot_to_int(mot):

    #h(w) = somme(ci * 31^(n-i)) mod 2^32

    n = len(mot) - 1
    val_hash = 0
    modulo = 2 ** 32
    
    for i, char in enumerate(mot):
        ci = ord(char)
        power = n - i
        big = pow(31, power, modulo)
        term = (ci * big) % modulo

        val_hash = (val_hash + term) % modulo
    
    return val_hash

def creer_dico(lg=0):
    return tp6_ex1_ex2.TableHachage(
        lg=lg,
        h=mot_to_int,
        h1=tp6_ex1_ex2.hash1b,
        h2=tp6_ex1_ex2.hash2b,
        tmin=0.25,
        tmax=0.75
    )

def ajouter_mot(dico, mot):
    return tp6_ex1_ex2.inserer(dico, mot)

def retirer_mot(dico, mot):
    return tp6_ex1_ex2.supprimer(dico, mot)

def dans_dico(dico, mot):
    pos = tp6_ex1_ex2.rechercher(dico, mot)
    return pos is not None

##############################################################
#
# crée un générateur des mots contenus dans le roman de Marcel Proust
#
def proust():
    with open("proust.txt", encoding="utf-8") as f:
        for ligne in f:
            for fragment in ligne.split('---'):
                for mot in fragment.split():
                    tmp = mot.strip('-,.?!;:"«»()‹›').lower()
                    if tmp != '' : yield tmp


##############################################################
#
# Main
#

if __name__ == '__main__':
    from time import time
    from ea4lib import printcol
    
    # Test 1: Création d'un dictionnaire et insertion des mots de Proust
    printcol("{Test 1: Création du dictionnaire et insertion des mots de Proust}", 'bold')
    debut = time()
    dico = creer_dico(1024)  # Taille initiale raisonnable
    
    # Ensemble pour éliminer les doublons
    mots_uniques = set()
    count = 0
    
    # Parcourir les mots et les ajouter à l'ensemble
    for mot in proust():
        mots_uniques.add(mot)
        count += 1
        if count % 10000 == 0:
            print(f"  {count} mots traités...")
    
    print(f"  Total: {count} mots dans le texte")
    print(f"  Nombre de mots uniques: {len(mots_uniques)}")
    
    # Insérer les mots uniques dans le dictionnaire
    for mot in mots_uniques:
        dico = ajouter_mot(dico, mot)
    
    fin = time()
    print(f"  Temps d'insertion: {fin - debut:.2f} secondes")
    print(f"  Taille finale du dictionnaire: {dico.lg}")
    print(f"  Taux de remplissage: {dico.nbCles / dico.lg:.2f}")
    
    # Test 2: Recherche de mots
    printcol("\n{Test 2: Vérification de mots dans le dictionnaire}", 'bold')
    mots_a_tester = ["amour", "temps", "marcel", "proust", "algorithme", "hachage"]
    
    for mot in mots_a_tester:
        if dans_dico(dico, mot):
            print(f"  '{mot}' est présent dans le dictionnaire")
        else:
            print(f"  '{mot}' n'est PAS présent dans le dictionnaire")
    
    # Test 3: Suppression et réinsertion
    printcol("\n{Test 3: Suppression et réinsertion}", 'bold')
    mots_a_supprimer = list(mots_uniques)[:5]  # Prendre les 5 premiers mots
    
    print("  Mots à supprimer:", mots_a_supprimer)
    
    for mot in mots_a_supprimer:
        print(f"  Suppression de '{mot}'")
        dico = retirer_mot(dico, mot)
        
        if not dans_dico(dico, mot):
            print(f"    '{mot}' a bien été supprimé")
        else:
            print(f"    ERREUR: '{mot}' est toujours présent")
    
    print("\n  Réinsertion des mots supprimés")
    for mot in mots_a_supprimer:
        dico = ajouter_mot(dico, mot)
        
        if dans_dico(dico, mot):
            print(f"    '{mot}' a bien été réinséré")
        else:
            print(f"    ERREUR: '{mot}' n'a pas été réinséré")
            
    # Test 4: Statistiques finales
    printcol("\n{Test 4: Statistiques finales}", 'bold')
    print(f"  Nombre de mots dans le dictionnaire: {dico.nbCles}")
    print(f"  Taille de la table: {dico.lg}")
    print(f"  Taux de remplissage: {dico.nbCles / dico.lg:.2f}")
    print(f"  Nombre de cases marquées: {dico.nbMarques}")
