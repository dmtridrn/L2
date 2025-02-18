#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>

size_t nbr_occ(int *t, size_t nbr, int v){
    size_t cpt = 0;
    for(int i = 0; i < nbr; i++){
        if(t[i] == v){
            cpt++;
        }
    }
    return cpt;
}

void nbr_occ_op(int *t, size_t nbr, int v, size_t *pnv){
    size_t cpt = 0;
    for(int i = 0; i < nbr; i++){
        if(t[i] == v){
            cpt++;
        }
    }
    *pnv = cpt;
}

void min_max_op(int *t, size_t nbr, int *pmin, int *pmax){
    int max = t[0];
    int min = t[0];
    for(int i = 1; i < nbr; i++){
        if(t[i]>max){
            max = t[i];
        }
        if(t[i] < min){
            min = t[i];
        }
    }
    *pmax = max;
    *pmin = min;
}

int main(){
    int tab[] = {90,20,30,3,4,5,3,3};
    size_t res = 0;
    int max = 0;
    int min = 0;
    nbr_occ_op(tab, 8, 3, &res);
    printf("%li\n", res);
    min_max_op(tab, 8, &min, &max);
    printf("min: %i, max: %i\n", min, max);
}