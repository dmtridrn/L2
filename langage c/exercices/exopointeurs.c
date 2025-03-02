#include<stdio.h>
#include<stdlib.h>

int somme(int* a, int* b){
    int somme = *a + *b;
    return somme;
}

int compare(int *a, int *b){
    if(*a == *b){
        return *a;
    }
    else if (*a < *b){
        return *b;
    }
    else{
        return *a;
    }
}

void affichetab(int taille, int t[]){
    for(int i = 0; i<taille; i++){
        printf("position %d: %d\n", i, t[i]);
    }
}

int max(int t[], int taille){
    int max = t[0];
    for(int i = 1; i<taille; i++){
        if(t[i] > max){
            max = t[i];
        }
    }
    return max;
}
int main(){
    int taille;
    printf("taille du tableau\n");
    scanf("%d", &taille);
    int tab[taille];
    for(int i = 0; i<taille; i++){
        printf("\nélément %i: ",i);
        scanf("%d", &tab[i]);
    }
    affichetab(taille, tab);
}