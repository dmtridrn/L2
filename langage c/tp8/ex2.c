#include"ex1.c"

maillon *produit_monome(maillon *p, int c, int d){
    maillon *res = creer_monome(p->coef * c, p->degre + d);
    return res;
}

maillon *produit(maillon *p1, maillon *p2){
    maillon *curr1 = p1;
    maillon *res;
    while(curr1 != NULL){
        maillon *curr2 = p2;
        
    }
}