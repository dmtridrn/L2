#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>

void print_tab1(int *t, size_t start, size_t end){
    for(int i = start; i < end; i++){
        int *adr = &t[i];
        int val = t[i];
        printf("%p : %i\n", adr, val);
    }
}

void print_tab2(int *pstart, int *pend){
    for(int* i = pstart; i < pend; i++){
        int *adr = i;
        int val = *i;
        printf("%p : %i\n", adr, val);
    }
}

int main(){
    int tab[] = {9,3,6,1,5,2};
    print_tab1(tab, 2, 6);
    printf("////////////////\n");
    print_tab2(tab+2, tab + 6);
}