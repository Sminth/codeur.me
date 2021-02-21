""" -*- coding: utf-8 -*-
Auteur: Emmanuel Malan
date : 11-12-20  ;  langage : python
objet : fonctions pour trouver le maximum 
et le minimum d'une liste d'entier et aussi
des fonctions pour trouver leur indice """

def maximum(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi

def minimum(liste):
    maxi = liste[0]
    for i in liste:
        if i <= maxi:
            maxi = i
    return maxi

def dernierIndiceMaximum(liste):
    maxi = liste[0]
    longueur=len(liste)
    indice_max = 0
    for i in range(longueur):
        if liste[i] >= maxi:
            maxi = liste[i]
            indice_max = i
    return indice_max

def dernierIndiceMinimum(liste):
    maxi = liste[0]
    longueur=len(liste)
    indice_max = 0
    for i in range(longueur):
        if liste[i] <= maxi:
            maxi = liste[i]
            indice_max = i
    return indice_max

#Exemple d'utilisation
l=[1,5,78,5,0]
print (maximum(l))
print (minimum(l))
print (dernierIndiceMaximum(l))
print (dernierIndiceMinimum(l))
