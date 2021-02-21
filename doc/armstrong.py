"""
Auteur: Emmanuel Malan
date : 13-09-19 ; langage : python
objet :nombre d'armstrong"""


def arms(n):
    """affiche si <n> est un nombre d'armstrong ou pas
153, 370, 371, 407 sont des nombres d'ARMSTRONG"""
    val=n
    arm_num = 0
    while (val > 0) :
        reminder = val % 10
        arm_num += reminder ** 3
        val //= 10

    if (int (n) == arm_num):
        print (n, "est un nombre d'ARMSTRONG")
    else:
        print (n, "n'est pas un nombre d'armstrong")


def nombres_arms():
    """affiche les nombres d'armstong compris entre 0 et 1000"""
    t=[]
    for n in range (1000):
        val=n
        arm_num = 0
        while (val > 0) :
            reminder = val % 10
            arm_num += reminder ** 3
            val //= 10

        if (int (n) == arm_num):
            t.append(n)
    print ("nombres d'armstrong compris entre 0 et 1000 :",t)

#programme principale
arms(350)
nombres_arms()
            
