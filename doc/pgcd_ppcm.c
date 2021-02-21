#include <stdio.h>
/*Auteur: Emmanuel Malan
date : 09-09-19 ; langage : c
objet : exemple de fonctions permettant de calculer le pgcd et le ppcm d'un nombre */

//Fonction de calcul du pgcd par l'algorithme d'euclide
int pgcd(int a, int b){ 
	int r;
    while (b!=0){
        r=a%b ;
        a=b ; b=r ;
    }
    return a ;
}

//Fonction de calcul du pgcd par soustraction
int pgcd_2(int a, int b){
    while (a!=b){
        if(a<b)
            b=b-a ;
        else
            a=a-b;
        }
    return a ;
}
//Fonction de calcul du ppcm
int ppcm(int a, int b){
	return (a * b) / pgcd(a,b);
}

//Programme Principale
main(){
	printf("pgcd(6,4)=%d \n",pgcd(6,4));
	printf("pgcd(12,24)=%d \n",pgcd_2(12,24));
	printf("ppcm(6,4)=%d \n",ppcm(6,4));
}
