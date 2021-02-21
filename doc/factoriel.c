#include "stdio.h"

/*
Auteur: Emmanuel Malan
date : 09-09-19 ; langage : C
#objet : exemple de fonctions permettant de calculer le factoriel d'un entier
*/

//fonction factorielle recursive
int fact(int n){
    //fact(int n): calcule la factorielle de n(entier >= 0)
    if(n<2)
        return 1;
    else
        return n*fact(n-1);
    }

//fonction factorielle non recursive avec la boucle for
int fact_2(int n){
    int x=1,i;
    for(i=2;i<n+1;i++){
		x*=i;
		}
    return x;
	}

//fonction factorielle non recursive avec la boucle while
int fact_3(int n){
    int resultat=1;
    while (n > 1){
        resultat = resultat * n;
        n= n- 1;
    }
    return resultat;
}

//Programme principale
main(){
	printf("(1)le factoriel de 3 est %d \n",fact(3));
	printf("(2)le factoriel de 5 est %d \n",fact_2(5));
	printf("(3)le factoriel de 0 est %d \n",fact_3(0));
}
