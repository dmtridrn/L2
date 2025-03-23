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

int main() {
    // Initialiser un w_index manuellement
    w_index *index = malloc(sizeof(w_index));
    
    // Définir 3 mots
    index->nbr = 3;
    index->words = malloc(index->nbr * sizeof(char*));
    
    // Allouer et initialiser chaque mot
    index->words[0] = malloc(6); // "Hello"
    strcpy(index->words[0], "Hello");
    
    index->words[1] = malloc(6); // "World"
    strcpy(index->words[1], "World");
    
    index->words[2] = malloc(5); // "Test"
    strcpy(index->words[2], "Test");
    
    // Afficher l'index
    printf("Contenu de l'index :\n");
    print_index(index);
    
    // Tester concat_words
    printf("Test de concat_words :\n");
    char *concatenated = concat_words(index);
    printf("Chaîne concaténée : \"%s\"\n", concatenated);
    
    // Libérer la mémoire de la chaîne concaténée
    free(concatenated);
    
    // Libérer la mémoire de l'index
    printf("Libération de la mémoire...\n");
    free_index(index);
    printf("Mémoire libérée avec succès.\n");
    
    return 0;
}