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

int main(int argc, char *argv[]) {
    int nb_monomes_p1, nb_monomes_p2;
    printf("Entrez le nombre de monômes du premier polynôme: ");
    scanf("%d", &nb_monomes_p1);
    
    printf("Entrez le nombre de monômes du deuxième polynôme: ");
    scanf("%d", &nb_monomes_p2);
    
    if (nb_monomes_p1 <= 0 || nb_monomes_p2 <= 0) {
        printf("Les nombres de monômes doivent être positifs.\n");
        return 1;
    }
    
    maillon *poly1 = NULL;
    printf("\nCréation du premier polynôme (%d monômes):\n", nb_monomes_p1);
    for (int i = 0; i < nb_monomes_p1; i++) {
        int coef, degre;
        printf("Monôme %d - Coefficient: ", i+1);
        scanf("%d", &coef);
        printf("Monôme %d - Degré: ", i+1);
        scanf("%d", &degre);
        
        poly1 = ajouter_monome(poly1, coef, degre);
    }
    
    maillon *poly2 = NULL;
    printf("\nCréation du deuxième polynôme (%d monômes):\n", nb_monomes_p2);
    for (int i = 0; i < nb_monomes_p2; i++) {
        int coef, degre;
        printf("Monôme %d - Coefficient: ", i+1);
        scanf("%d", &coef);
        printf("Monôme %d - Degré: ", i+1);
        scanf("%d", &degre);
        
        poly2 = ajouter_monome(poly2, coef, degre);
    }
    
    printf("\nPolynôme 1: ");
    afficher_polynome(poly1);
    
    printf("Polynôme 2: ");
    afficher_polynome(poly2);
    
    printf("Somme des polynômes: ");
    maillon *somme_poly = somme(poly1, poly2);
    afficher_polynome(somme_poly);
    
    liberer(poly1);
    liberer(poly2);
    liberer(somme_poly);
    
    return 0;
}