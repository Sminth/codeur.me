
def palin(nbr):
	
    nbrInverser = 0
    tmp = nbr
    while (tmp != 0):
    	nbrInverser = nbrInverser * 10
    	nbrInverser = nbrInverser + tmp%10
    	tmp = tmp/10
       
     
    if (nbr == nbrInverser):
        print ("{} est un nombre palindrome.\n".format(nbr))
    else:
        print ("{} n'est pas un nombre palindrome.\n".format(nbr))
     
    return 0


####Programme principale
nbre=int (input ("Entrez un nombre pour verifier s'il s'agit d'un palindrome ou non\n"))
palin(nbre)
