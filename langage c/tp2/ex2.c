#include<stdio.h>
#include<stdlib.h>
#include <stdbool.h>
#define SUP 1000000

void affichetab(int T[], int longueur){
	printf("[");
	for(int i = 0; i<longueur; i++){
		int a = T[i];
		if(longueur-1 == i){
			printf("%i",a);
		}
		else{
			printf("%i, ",a);
		}
	}
	printf("] \n");
}

void initialisation(bool t[], size_t n){
	for(int i = 0; i<n; i++){
		t[i] = true;
	}
}

void remplissage(bool t[], size_t n){
	for(int i = 2; i<SUP; i++){
		if(t[i]){
			for(int j = 2*i; j<SUP; j+=i){
				t[j] = false;
			}
		}
	}
}

void affichNbpremier(bool t[], size_t n){
	int longueur = 0;
	for(int i = 0; i<SUP; i++){
		if(t[i]){
			longueur++;
		}
	}
	int f[longueur];
	for(int i = 0; i<longueur;i++){
		f[i] = 0;
	}
	int cpt = 0;
	for(int i = 0; i<SUP; i++){
		if(t[i]){
			f[cpt] = i;
			cpt++;
		}
	}
	affichetab(f,longueur);
}


int main(){
	bool t[SUP] = {};
	initialisation(t,SUP);
	remplissage(t, SUP);
	affichNbpremier(t,SUP);
}