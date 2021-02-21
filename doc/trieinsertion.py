""" -*- coding: utf-8 -*-
Auteur: Emmanuel Malan
date : 11-12-20  ;  langage : python
objet : fonction du trie par insertion """

def trieParInsertion(liste):
    for index in range(len(liste)): #on parcourt la liste
        item = liste[index]         #un élément de la liste
        j = index
        while j>0 and liste[j-1] > item: #tant qu'on n'a pas atteint le début ou un élément plus petit
            liste[j] = liste[j-1]        #on décale l'élément trouvé vers la droite
            j=j-1
        liste[j]=item       #on insere item a sa place
    return liste


#Exemple d'utilisation
l=[1,5,78,5,0]
print (trieParInsertion(l))
