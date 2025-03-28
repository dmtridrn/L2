#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>
#include <math.h>

typedef struct maillon{
    int coef;
    int degre;
    struct maillon *suiv;
} maillon;

maillon *creer_monome(int c, int d){
    maillon *res = malloc(sizeof(maillon));
    if (res == NULL){
        return NULL;
    }
    res->coef = c;
    res->degre = d;
    res->suiv = NULL;
    return res;
}

void liberer(maillon *p){
    maillon *curr = p;
    while(curr != NULL){
        p = curr->suiv;
        free(curr);
        curr = p;
    }
}

double evaluer_polynome(maillon *p, double x){
    double res = 0.0;
    maillon *curr = p;
    while(curr != NULL){
        res += ((curr->coef)* pow(x,curr->degre));
        curr = curr->suiv;
    }
    return res;
}

void afficher_polynome(maillon *p){
    maillon *curr = p;
    while(curr != NULL){
        if(curr->degre == 0){
            printf("%i",curr->coef);
        }
        else if(curr->degre == 1){
            printf("%iX + ",curr->coef);
        }
        else{
            printf("%iX^%i + ",curr->coef, curr->degre);
        }
        curr = curr->suiv;
    }
    puts("");
}

maillon *ajouter_monome(maillon *p , int c, int d){
    if(p == NULL){
        return creer_monome(c,d);
    }
    if(d > p->degre){
        maillon *nv = creer_monome(c,d);
        nv->suiv = p;
        return nv;
    }
    else{
        maillon *curr = p;
        while(curr->suiv != NULL && curr->suiv->degre > d){
            curr = curr->suiv;
        }
        if(curr->suiv == NULL){
            maillon *nv = creer_monome(c,d);
            curr->suiv = nv;
            return p;
        }
        if(curr->suiv->degre != d){
            maillon *nv = creer_monome(c,d);
            nv->suiv = curr->suiv;
            curr->suiv = nv;
            return p;
        }
        else{
            curr->suiv->coef += c;
            if(curr->suiv->coef == 0){
                curr->suiv = curr->suiv->suiv;
            }
            return p;
        }
    }
}

maillon *copie(maillon *p){
    if(p == NULL){
        return NULL;
    }
    maillon *tete = creer_monome(p->coef, p->degre);
    maillon *curr = p->suiv;
    maillon *tmp = tete;
    while(curr!= NULL){
        tmp->suiv = creer_monome(curr->coef, curr->degre);
        curr = curr->suiv;
        tmp = tmp->suiv;
    }
    return tete;
}

maillon *somme(maillon *p1, maillon *p2){
    if (p1 == NULL) return copie(p2);
    if (p2 == NULL) return copie(p1);
    
    maillon *tete;
    maillon *courant;
    maillon *curr1 = p1;
    maillon *curr2 = p2;
    
    if(curr1->degre > curr2->degre){
        tete = creer_monome(curr1->coef, curr1->degre);
        curr1 = curr1->suiv;
    }
    else if(curr1->degre == curr2->degre){
        tete = creer_monome(curr1->coef + curr2->coef, curr1->degre);
        curr1 = curr1->suiv;
        curr2 = curr2->suiv;
    }
    else{
        tete = creer_monome(curr2->coef, curr2->degre);
        curr2 = curr2->suiv;
    }
    
    courant = tete; 
    
    while(curr1 != NULL && curr2 != NULL){
        if(curr1->degre == curr2->degre){
            courant->suiv = creer_monome(curr1->coef + curr2->coef, curr1->degre);
            curr1 = curr1->suiv;
            curr2 = curr2->suiv;
        }
        else if(curr1->degre > curr2->degre){
            courant->suiv = creer_monome(curr1->coef, curr1->degre);
            curr1 = curr1->suiv;
        }
        else{
            courant->suiv = creer_monome(curr2->coef, curr2->degre);
            curr2 = curr2->suiv;
        }
        courant = courant->suiv;
    }
    
    while(curr1 != NULL){
        courant->suiv = creer_monome(curr1->coef, curr1->degre);
        curr1 = curr1->suiv;
        courant = courant->suiv;
    }
    
    while(curr2 != NULL){
        courant->suiv = creer_monome(curr2->coef, curr2->degre);
        curr2 = curr2->suiv;
        courant = courant->suiv;
    }
    
    return tete;
}

int main() {
    // Création d'un polynôme initial 5x^3 + 7x^2 + 2x + 3
    maillon *poly = creer_monome(5, 3);  // 5x^3
    poly = ajouter_monome(poly, 7, 2);   // + 7x^2
    poly = ajouter_monome(poly, 2, 1);   // + 2x
    poly = ajouter_monome(poly, 3, 0);   // + 3
    
    printf("Polynôme original : ");
    afficher_polynome(poly);
    
    // Création d'une copie du polynôme
    maillon *poly_copie = copie(poly);
    printf("Polynôme copié : ");
    afficher_polynome(poly_copie);
    
    // Modification du polynôme original
    poly = ajouter_monome(poly, 4, 4);   // Ajout de 4x^4
    poly = ajouter_monome(poly, -2, 1);  // Modification de 2x à 0x
    
    // Vérification que les deux polynômes sont différents
    printf("\nAprès modifications :\n");
    printf("Polynôme original modifié : ");
    afficher_polynome(poly);
    printf("Polynôme copié (doit rester intact) : ");
    afficher_polynome(poly_copie);
    
    // Évaluation des deux polynômes pour x=2
    printf("\nÉvaluation pour x=2 :\n");
    printf("Original : %f\n", evaluer_polynome(poly, 2.0));
    printf("Copie : %f\n", evaluer_polynome(poly_copie, 2.0));
    printf("Addition: ");
    maillon *sum = somme(poly, poly_copie);
    afficher_polynome(sum);
    
    // Libération de la mémoire
    liberer(poly);
    liberer(poly_copie);
    liberer(sum);
    
    return 0;
}