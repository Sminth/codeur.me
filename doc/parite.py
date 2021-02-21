"""
Auteur: Emmanuel Malan
date : 09-09-19 ; langage : python
objet : procedure qui verifie la parité d'un nombre
"""

def parité(n):
    if n%2 == 0:
        #le symbole (%) est le modulo qui exprime le reste de la division de n par 2
        
        print(n, "est pair.")
    else:
        print(n, "est impair.")


parité(5)   #appel de la procedure parité
