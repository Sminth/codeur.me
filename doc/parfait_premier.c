#include "stdio.h"
/*
Auteur: Emmanuel Malan
date : 12-09-19 ; langage : c
objet : programme qui verifie si un  nombre est premier ou s'il est parfait 
*/

int somDiv(int n){
    /*Retourne la somme des diviseurs propres de <n>.
       On appelle diviseur propre de n, un diviseur quelconque de n, n exclu*/

    int i,somme = 1;
    for(i=2;i<n/2+1;i++){
        if((n % i) == 0) somme += i;
        }
    return somme;
}
estParfait(int n){
       /*Teste si <n> est parfait.
       un entier naturel est dit parfait s’il est égal à
       la somme de tous ses diviseurs propres*/
    
    if (somDiv(n) == n)  printf("%d est parfait\n",n);
    else printf("%d est imparfait\n",n);
}
estPremier(int n){
      /*Teste si <n> est premier.
       On appelle nombre premier tout entier naturel supérieur à
       1 qui possède exactement deux diviseurs, lui-même et l’unité*/
    
    if (somDiv(n) == 1)  printf("%d est premier\n",n);
    else printf("%d n'est pas premier\n",n);
}
//Programme principale
main(){
	estParfait(15);
	estPremier(3);
}


