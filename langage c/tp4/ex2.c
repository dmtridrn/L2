#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>

size_t occ(int *t, size_t nbr, int v){
	for(size_t i = 0; i<nbr; i++){
		if(t[i] == v){
			return i;
		}
	}
	return nbr;
}

int *occ_ptr(int *t, size_t nbr, int v){
	for(size_t i = 0; i<nbr; i++){
		if(t[i] == v){
			return &t[i];
		}
	}
	return NULL;
}

int main(){
	int tab[] = {1,2,3,4};
	int *occur = occ_ptr(tab, 4, 1);
	int occure = occ(tab,4,3);
	printf("%i\n", occure);
	printf("%p\n", occur);
}