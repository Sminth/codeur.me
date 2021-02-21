""" -*- coding: utf-8 -*-
Auteur: Emmanuel Malan
date : 09-09-19 ; langage : python
objet : exemple de fonctions permettant de calculer le pgcd et le ppcm d'un nombre
"""

# Fonction de calcul du pgcd par l'algorithme d'euclide
def pgcd(a,b):
    
    while (b!=0):
        r=a%b
        a,b=b,r
    return a

# Fonction de calcul du pgcd par soustraction
def pgcd_2(a,b):
    while (a!=b):
        if(a<b):
            b=b-a
        else:
            a=a-b
    return a

# Fonction de calcul du ppcm
def ppcm(a,b):
	return (a * b) / pgcd(a,b)


#exemple d'utilisation
print(pgcd(6,4))
print(pgcd_2(6,4))
print(ppcm(6,4))
