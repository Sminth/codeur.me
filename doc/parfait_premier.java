package codeur.com;
/*
Auteur: Emmanuel Malan
date : 12-09-19 ; langage : c
objet : programme qui verifie si un  nombre est premier ou s'il est parfait
*/
public class parfait_premier {

	public static void main(String[] args) {
		//programme principale
		estParfait(15);
		estPremier(3);

	}

	static int somDiv(int n){
	    /*Retourne la somme des diviseurs propres de <n>.
	       On appelle diviseur propre de n, un diviseur quelconque de n, n exclu*/

	    int i,somme = 1;
	    for (i=2;i<n/2+1;i++){
	        if ((n % i) == 0) somme += i;
	        }
	    return somme;
}
	static void estParfait(int n){
	       /*Teste si <n> est parfait.
	       un entier naturel est dit parfait s'il est egal a
	       la somme de tous ses diviseurs propres*/

	    if (somDiv(n) == n)  System.out.println (n+" est parfait\n");
	    else System.out.println (n+" est imparfait\n");
	}
	static void estPremier(int n){
	      /*Teste si <n> est premier.
	       On appelle nombre premier tout entier naturel superieur a
	       1 qui possede exactement deux diviseurs, lui-même et l'unit�*/

	    if (somDiv(n) == 1)  System.out.println (n+" est premier\n");
	    else System.out.println(n+" n'est pas premier\n");
	}
}
