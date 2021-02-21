package codeur.com;
/*Auteur: Emmanuel Malan
date : 15-09-19 ; langage : java
objet : exemple de fonctions permettant de calculer le pgcd et le ppcm d'un nombre */


public class pgcd_ppcm {
	public static void main(String[] args) {
		//Programme principale
		System.out.println ("pgcd(6,4)= "+pgcd(6,4)+"\n");
		System.out.println ("pgcd(12,24)= "+pgcd_2(12,24)+"\n");
		System.out.println ("ppcm(6,4)= "+ppcm(6,4)+"\n");
	}

	//Fonction de calcul du pgcd par l'algorithme d'euclide
	static int pgcd(int a, int b){
			int r;
		    while (b!=0){
		        r=a%b ;
		        a=b ; b=r ;
		    }
		    return a ;
		}

	//Fonction de calcul du pgcd par soustraction
	static int pgcd_2(int a, int b){
		    while (a!=b){
		        if (a<b)
		            b=b-a ;
		        else
		            a=a-b;
		        }
		    return a ;
		}
	//Fonction de calcul du ppcm
	static int ppcm(int a, int b){
			return (a * b) / pgcd(a,b);
		}
}
