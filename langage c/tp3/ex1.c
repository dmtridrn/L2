#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<time.h>

#define NBC 5


enum etat{
	VALIDEE, ENCOURS, EXPEDIEE
};
typedef enum etat etat;

struct commande{
	int num_com;
	int prix_exp;
	int prix_prod;
	etat etat_com;
};
typedef struct commande commande;

commande com_alea(int num){
	int numero = num;
	int prix_expedition = rand()%20 + 1;
	int prix_produit = rand()%2000 + 1;
	int etat = rand()%3;

	commande com = {.num_com = numero, .prix_exp = prix_expedition, 
					.prix_prod = prix_produit, .etat_com = etat};
	return com;
}

void affiche_com(commande c){
	printf("numéro de commande: %i\n", c.num_com);
	printf("prix expedition: %i\n", c.prix_exp);
	printf("prix produit: %i\n", c.prix_prod);
	switch(c.etat_com){
		case VALIDEE:
			printf("VALIDEE\n"); break;
		case ENCOURS:
			printf("EN COURS\n"); break;
		case EXPEDIEE:
			printf("EXPEDIEE\n"); break;
	}
}

void affiche_exp(commande t[], size_t taille){
	for(int i = 0; i<taille; i++){
		if(t[i].etat_com == 2){
			affiche_com(t[i]);
		}
	}
}

int nbr_en_cours(commande t[], size_t taille){
	int cpt = 0;
	for(int i = 0; i<taille; i++){
		if(t[i].etat_com == 1){
			cpt++;
		}
	}
	return cpt;
}

int cout_vaildees(commande t[], size_t taille){
	int cpt = 0;
	for(int i = 0; i<taille; i++){
		if(t[i].etat_com == 2){
			cpt+=t[i].prix_exp;
		}
	}
	return cpt;
}


int main(){
	srand(time(NULL));
	commande com2 = {.num_com = 2, .prix_exp = 60, .prix_prod = 50, .etat_com = ENCOURS};
	commande com3 = com_alea(3);

	commande c[NBC] = {};
	for(int i = 1; i<NBC; i++){
		c[i] = com_alea(i);
		//affiche_com(c[i]);
	}
	//printf("%i\n", nbr_en_cours(c,NBC));
	//printf("%i\n", cout_vaildees(c,NBC));
}

/*
QUESTION 8:
	
	oui, il est possible d'écrire une fonction telle que le code affiche 200 avec:
	
	void change_prix(commande c, int nvprix){
		c.prix_prod = nvprix;
	}

QUESTION 9:

	oui avec:

	void expedie_tout(commande tab[], size_t n){
		for(int i = 0; i<n; i++){
			tab[i].etat_com = EXPEDIEE;
		}
	}

*/


