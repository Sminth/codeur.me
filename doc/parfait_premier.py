"""
Auteur: Emmanuel Malan
date : 12-09-19 ; langage : python
objet : programme qui verifie si un  nombre est premier ou s'il est parfait 
"""

def somDiv(n):
    """Retourne la somme des diviseurs propres de <n>.
       On appelle diviseur propre de n, un diviseur quelconque de n, n exclu"""
    
    somme = 1
    for i in range(2, n//2+1):
        if(n % i) == 0:
            somme += i
    return somme

def estParfait(n):
    """Teste si <n> est parfait.
       un entier naturel est dit parfait s’il est égal à
       la somme de tous ses diviseurs propres"""
    
    if somDiv(n) == n:
        print(n,"est parfait")
    else:
        print(n,"est imparfait")
def estPremier(n):
    """Teste si <n> est premier.
       On appelle nombre premier tout entier naturel supérieur à
       1 qui possède exactement deux diviseurs, lui-même et l’unité"""
    
    if somDiv(n) == 1 :
        print(n,"est premier")
    else:
        print(n,"n'est pas premier")


estParfait(15)
estPremier(3)
