""" -*- coding: utf-8 -*-
Auteur: Emmanuel Malan
date : 11-12-20  ;  langage : python
objet : recherche sequentielle """

def recherche_sequentielle(liste, element):
    a=0;
    b =len (liste)
    trouve = False
    i=a
    while ( trouve == False and i<b):
        if liste[i] == element :
            trouve = True
        i=i+1
    return trouve

# Programme principale pour tester le code ci-dessus
tab = [1, 22, 23, 74]
 
print (recherche_sequentielle(tab,15)) 
