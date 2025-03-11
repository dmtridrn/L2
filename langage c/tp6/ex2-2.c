#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>

char *multiplier(const char *s, unsigned n){
    size_t len = strlen(s);
    char *c = malloc(n*len + 1);
    if(c == NULL){
        return NULL;
    }
    size_t pos = 0;
    for(unsigned i = 0; i < n; i++){
        memmove(c + pos, s, len);
        pos += len;
    }
    c[n*len] = '\0';
    return c;
}

int main(int argc, char *argv[]){
    if(argc != 3){
        puts("il faut 2 arguments");
    }
    unsigned mult = atoi(argv[2]);
    if(mult == 0){
        puts("veuillez rentrer un int > 0 en deuxième arg");
        return EXIT_FAILURE;
    }
    char *x = multiplier(argv[1], mult);
    printf("%s\n", x);
    return EXIT_SUCCESS;
}