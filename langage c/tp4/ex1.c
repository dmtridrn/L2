#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>

void swap(int *p, int *q){
	int tmp = *p;
 	*p = *q;
 	*q = tmp;
 	return;
}

void affichetab(int T[]){
	int longueur = 5;
	printf("[");
	for(int i = 0; i<longueur; i++){
		int a = T[i];
		printf("%i ",a);
	}
	printf("] \n");
}

int main(){
	int tab[] = {1,2,3,4,5};
	affichetab(tab);
	swap(&tab[4], tab);
	affichetab(tab);
	return 0;
}