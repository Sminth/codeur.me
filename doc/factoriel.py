""" -*- coding: utf-8 -*-
Auteur: Emmanuel Malan
date : 09-09-19
langage : python
objet : exemple de fonctions permettant de calculer le factoriel d'un entier fonction recursive, itteratif_bouble_for, itteratif_bouble_while
"""


#fonction factorielle recursive
def fact(n):
    """fact(n): calcule la factorielle de n(entier >= 0)"""
    if n<2:
        return 1
    else:
        return n*fact(n-1)

#fonction factorielle non recursive avec la boucle for
def fact_2(n):
    """fact_2(n): calcule la factorielle de n (entier >= 0)"""
    x=1
    for i in range(2,n+1):
        x*=i
    return x

#fonction factorielle non recursive avec la boucle while
def fact_3(n):
    """fact_2(n): calcule la factorielle de n (entier >= 0)"""
    resultat=1
    while  (n > 1) :
        resultat = resultat * n
        n= n- 1
    return resultat

# Exemple d'utilisation:
print(fact(3))
print(fact_2(3))
print(fact_3(3))
