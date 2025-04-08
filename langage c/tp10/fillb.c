#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>

int main(int argc, char *argv[]){
    assert(argc == 2);
    char *fic = argv[1];
    FILE* file = fopen(fic, "w");
    assert(file != NULL);

    int c;
    while((c = fgetc(stdin)) != EOF){
        fputc(c,file);
    }

    fclose(file);
}