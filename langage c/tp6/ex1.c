#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>

char *dupliquer(const char *s){
    char *c = malloc(strlen(s)+1);
    if(c == NULL){
        return NULL;
    }
    memmove(c, s, strlen(s)+1);
    return c;
}

int ordrealpha(const char *s1, const char *s2) {
    int i = 0; 
    while(s1[i] != '\0' && s2[i] != '\0') {
        if(s1[i] > s2[i]) {
            return 1;
        }
        else if(s1[i] < s2[i]) {
            return -1;
        }
        i++;
    }
    if(s1[i] == '\0' && s2[i] != '\0') {
        return -1;
    }
    else if(s1[i] != '\0' && s2[i] == '\0') {
        return 1;
    }
    return 0;
}

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