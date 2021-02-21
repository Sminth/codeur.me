package codeur.com;
/*
Auteur: Emmanuel Malan
date : 15-09-19 ; langage : java
objet : procedure qui verifie la parit� d'un nombre
*/
public class parite {

	public static void main(String[] args) {
		//Programme principale
		parite(5);   //appel de la procedure parit�
		parite(10);
	}

	static void parite(int n){

		    if (n%2 == 0){
		        //le symbole (%) est le modulo qui exprime le reste de la division de n par 2
		        System.out.println (n+" est pair.\n");
		    }
		    else  System.out.println (n+" est impair.\n");
		}

}
