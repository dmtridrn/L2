#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>
#define LENGTH 9

void swap(int *p, int *q){
	int tmp = *p;
 	*p = *q;
 	*q = tmp;
 	return;
}

void affichetab(int T[]){
	printf("[");
	for(int i = 0; i<LENGTH; i++){
		int a = T[i];
		printf(" %i ",a);
	}
	printf("] \n");
}

void sort (int *t, size_t start, size_t end){
    for(int i = end-1; i > start; i--){
        for(int j = 0; j < i; j++){
            if(t[j] > t[j+1]){
                swap(&t[j], &t[j+1]);
            }
        }
    }
}

void sort_ptr (int *start, int *end){
    for(int *i = end-1; i > start; i--){
        for(int *j = start; j < i; j++){
            if(*j > *(j+1)){
                swap(j, j+1);
            }
        }
    }
}

int main(){
    int tab[] = {7,9,4,3,2,10,1,8};
    sort_ptr(tab, tab+9);
    affichetab(tab);
}