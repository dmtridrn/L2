#include<stdlib.h>
#include<stdio.h>

unsigned **pascal(int taille){
    if(taille > 0){
        unsigned **tp = calloc(taille, sizeof(unsigned *));
        if(tp == NULL){
            return NULL;
        }
        for (size_t i = 0; i < taille; i++){
            *(tp + i) = calloc(i+1, sizeof(unsigned));
            if(*(tp+i) == NULL){
                return NULL;
            }
            for(size_t j = 0; j<=i; j++){
                if(i == 0 || j == 0 || j == i){
                    *(*(tp+i)+j) = 1;
                }
                else{
                    *(*(tp+i)+j) = *(*(tp+i-1)+j-1) + *(*(tp+i-1)+j); 
                }
            }
        }
        return tp;
    }
    else{
        return NULL;
    }
}

void affichePascal(unsigned **t, size_t taille){
    for(size_t i = 0; i<taille; i++){
        for(size_t j = 0; j<=i; j++){
            printf("%u ", *(*(t+i)+j));
        }
        printf("\n");
    }
}

void libere_pascal(unsigned **t, size_t taille){
    for(size_t i = 0; i<taille; i++){
        free(*(t+i));
    }
    free(t);
}

int main(){
    size_t taille;
    puts("Entrez la taille du triangl désirée");
    scanf("%zu", &taille);
    printf("Triangle de pascal de taille %zu:\n", taille);
    unsigned **t = pascal(taille);
    affichePascal(t, taille);
    libere_pascal(t, taille);
}