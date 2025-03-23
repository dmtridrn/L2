#include"ex1.c" //atroce mais ça marche

typedef struct{
    int nbr;
    char **words;
} w_index;


void free_index(w_index *pi){
    for(unsigned i = 0; i<pi->nbr; i++){
        free(pi->words[i]);
    }
    free(pi->words);
    free(pi);
}

void print_index(w_index *pi){
    for(unsigned i = 0; i < pi -> nbr; i++){
        printf("Mot %u:  ", i+1);
        for(unsigned j = 0; pi -> words[i][j] != '\0'; j++){
            printf("%c", pi -> words[i][j]);
        }
        puts("\n");
    }
}

int size_words(w_index *pi){
    int cpt = 0;
    for(unsigned i = 0; i < pi -> nbr; i++){
        for(unsigned j = 0; pi -> words[i][j] != '\0'; j++){
            cpt++;
        }
    }
    return cpt;
}

char *concat_words(w_index *pi){
    char *concat = malloc(pi->nbr + size_words(pi));
    int indice = 0;
    for(unsigned i = 0; i < pi -> nbr; i++){
        for(unsigned j = 0; pi -> words[i][j] != '\0'; j++){
            concat[indice] = pi->words[i][j];
            indice++;
        }
        if(i+1 != pi->nbr){
            concat[indice] = ' ';
            indice ++;
        }
    }
    return concat;
}

w_index *cons_index(const char *s){
    w_index *index = malloc(sizeof(w_index));
    if (index == NULL) {
        return NULL;
    }
    
    index->nbr = nbr_words(s);
    
    index->words = malloc(index->nbr * sizeof(char*));
    if (index->words == NULL) {
        free(index);
        return NULL;
    }
    
    char *courant = (char *)s;
    int longueur = 0;
    
    for(unsigned i = 0; i < index->nbr; i++){
        courant = next_word(courant);
        if (courant == NULL) {
            for(unsigned j = 0; j < i; j++) {
                free(index->words[j]);
            }
            free(index->words);
            free(index);
            return NULL;
        }
        
        index->words[i] = extract_word(courant, &longueur);
        if (index->words[i] == NULL) {
            for(unsigned j = 0; j < i; j++) {
                free(index->words[j]);
            }
            free(index->words);
            free(index);
            return NULL;
        }
        
        courant += longueur;
    }
    
    return index;
}

int main() {
    char *str = "      aaa     b     cecece ";
    
    w_index *user_index = cons_index(str);
    if (user_index == NULL) {
        printf("Erreur lors de la création de l'index\n");
        return 1;
    }
    
    printf("Index créé à partir de la chaîne \"%s\":\n", str);
    print_index(user_index);
    
    char *user_concat = concat_words(user_index);
    printf("Chaîne reconstruite : \"%s\"\n", user_concat);
    
    free(user_concat);
    free_index(user_index);
    printf("Mémoire libérée avec succès.\n");
    
    return 0;
}