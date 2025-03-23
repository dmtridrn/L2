#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>

int nbr_words(const char *s){
    unsigned cpt = 0;
    bool in_word = false;
    
    for(size_t i = 0; s[i] != '\0'; i++){
        if (!isspace(s[i])) {
            if (!in_word) {
                cpt++;
                in_word = true;
            }
        } else {
            in_word = false;
        }
    }
    
    return cpt;
}

int word_len(const char *w){
    assert(*w != ' ');
    size_t cpt = 0;
    while((!isspace(w[cpt])) && (w[cpt] != '\0')){
        cpt ++;
    }
    return cpt;
}

char *extract_word(const char *w, int *pl){
    assert(*w != ' ');
    int longueur = word_len(w);
    char *copie = malloc(longueur + 1);
    if(copie == NULL){
        return NULL;
    }
    memmove(copie, w, longueur);
    copie[longueur] = '\0';
    *pl = longueur;
    return copie;
}

char *next_word(char *w){
    unsigned i = 0;
    while(isspace(w[i]) && w[i] != '\0'){
        i++;
    }
    if(w[i] == '\0'){
        return NULL;
    }
    return w + i;
}