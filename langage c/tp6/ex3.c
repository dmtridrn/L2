#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>

typedef struct{
    size_t indice;
    size_t len;
} mutation;

int nboc(const char *s, const char *sub) {
    int cpt = 0;
    size_t len1 = strlen(s);
    size_t len2 = strlen(sub);
    for (size_t i = 0; i <= len1 - len2; i++) {
        bool match = true;
        for (size_t j = 0; j < len2; j++) {
            if (s[i + j] != sub[j]) {
                match = false;
                break;
            }
        }
        if (match) {
            cpt++;
        }
    }
    return cpt;
}

mutation diff(const char *s, const char *t){
    mutation m = {0, 0};
    int lenS = strlen(s);
    int lenT = strlen(t);
    assert(lenS == lenT);
    int cpt = 0;
    for(unsigned i = 0; i<lenS; i++){
        if(s[i] != t[i]){
            m.indice = i;
            for(unsigned j = i; j<lenT; j++){
                if(s[j] == t[j]){
                    break;
                }
                cpt++;
            }
            break;
        }
    }
    m.len = cpt;
    return m;
}

mutation longest(const char *s, const char *t){
    mutation longest = diff(s,t);
    size_t lenS = strlen(s);
    if(longest.len == 0){
        puts("pas de mutation");
        return longest;
    }
    int i = 0;
    while(longest.len + i < lenS){
        mutation temp = diff(s+i, t+i);
        if(temp.len > longest.len){
            temp.indice += i;
            longest = temp;
        }
        i++;
    }
    return longest;
}

char *longest_string(const char *s, const char *t){
    mutation m = longest(s,t);
    int i = m.indice;
    char *mutation = malloc(m.len+1);
    if(mutation == NULL){
        return NULL;
    }
    memmove(mutation, t+i, m.len);
    mutation[m.len] = '\0';
    return mutation;
}


int main(){
    char* str1 = "AAAAAAAAAAAA";
    char* str2 = "CCCCCCAAYYYY";

    mutation m1 = longest(str1, str2);
    char *a = longest_string(str1, str2);
    printf("indice: %zu, longueur: %zu\n", m1.indice, m1.len);
    printf("mutation: %s\n", a);
    free(a);
}