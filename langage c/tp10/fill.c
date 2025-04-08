#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>

int main(int argc, char *argv[]){
    if(argc != 3){
        fprintf(stderr, "Usage: %s <filename> <number_of_lines>\n", argv[0]);
        return 1;
    }
    
    char *filename = argv[1];
    int n = atoi(argv[2]);
    
    if(n <= 0){
        fprintf(stderr, "Error: Number of lines must be positive\n");
        return 1;
    }
    
    FILE *file = fopen(filename, "a");
    if(file == NULL){
        perror("Error opening file");
        return 1;
    }
    for(int i = 1; i <= n; i++){
        fprintf(file, "ligne %d / %d\n", i, n);
    }
    
    fclose(file);
    
    printf("FICHIER CRéé '%s' avec %d lignes \n", filename, n);
    
    return 0;
}