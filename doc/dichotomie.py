""" -*- coding: utf-8 -*-
Auteur: Emmanuel Malan
date : 11-12-20  ;  langage : python
objet : recherche dichotomique """

def recherche_dichotomique(liste_triee, element):
    a = 0
    b = len (liste_triee) - 1
    while a <= b:
        m = (a + b) // 2
        if liste_triee[m] == element:
            # on a trouve v
            return True
        elif liste_triee[m] < element:
            a = m + 1
        else:
            b = m - 1
    # on a a > b
    return False
# Programme principale pour tester le code ci-dessus
tab = [1, 15, 22, 74]
 
print (recherche_dichotomique(tab,22))  
