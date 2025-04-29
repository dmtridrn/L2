#include<stdio.h>
#include<stdlib.h>
#include<assert.h>
#include<stdbool.h>
#include<string.h>
#include<ctype.h>

typedef struct{
    int x,y;
} paire;

int main(){
    int a = 2;
    void *pt = &a;
    *((int*)pt) = 42;
    printf("%i\n", a);
    *((int*)pt) *= *((int*)pt);
    printf("%i\n", a);
    paire b = {.x = 1, .y = 3};
    printf("%i\n", b.y);
    pt = &b;
    ((paire*)pt) -> y = 4;
    printf("%i\n", b.y);
    return EXIT_SUCCESS;
}