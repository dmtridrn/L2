#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>

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

int main(int argc, char *argv[]){
    if(argc != 3){
        puts("il faut 2 arguments");
    }
    int res = ordrealpha(argv[1], argv[2]);
    if(res == 1){
        printf("%s > %s\n", argv[1], argv[2]);
    }
    else if(res == -1){
        printf("%s < %s\n", argv[1], argv[2]);
    }
    else{
        printf("%s = %s\n", argv[1], argv[2]);
    }
}