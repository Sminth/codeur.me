package codeur.com;
/*Auteur: Emmanuel Malan
date : 13-09-19 ; langage : java
#objet : exemple de fonctions permettant de calculer le factoriel d'un entier
*/
public class factoriel {

	//fonction factorielle recursive
	static int fact(int n){
	//fact(int n): calcule la factorielle de n(entier >= 0)

	    if (n<2)
	        return 1;
	    else
	        return n*fact(n-1) ;
	    }

	//fonction factorielle non recursive avec la boucle for
	static int fact_2(int n){
	    int x=1, i ;
	    for (i=2;i<n+1;i++){
			x*=i;
			}
	    return x;
		}

	//fonction factorielle non recursive avec la boucle while
	static int fact_3(int n){
	    int resultat = 1;
	    while (n > 1){
	        resultat = resultat * n;
	        n= n-1;
	    }
	    return resultat;
	}
	public static void main(String[] args) {
	//Programme principale
			System.out.println ("(1)le factoriel de 3 est "+fact(3));
			System.out.println ("(2)le factoriel de 5 est "+fact_2(5));
			System.out.println ("(3)le factoriel de 0 est "+fact_3(0));

	}
}
