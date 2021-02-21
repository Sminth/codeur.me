#include "stdio.h"
/*
Auteur: Emmanuel Malan
date : 12-09-19 ; langage : c
objet : procedure qui verifie la parité d'un nombre
*/

parite(int n){

    if(n%2 == 0){
        //le symbole (%) est le modulo qui exprime le reste de la division de n par 2
        printf("%d est pair.\n",n);
    }
    else  printf("%d est impair.\n",n);
}

//Programme principale
main(){
	parite(5);   //appel de la procedure parité
	parite(10);
}


