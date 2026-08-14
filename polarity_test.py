

""" EXERCICE 1: partie 2
demande a l'utilisateur de saisir un nombre.
utilise try / except pour verifer que la valeur saisie est bien un entier.
Ensuite :
    *si le nombre est positif, afficher :
    NOMBRE POSITIF
    *s'il est negatif
    NOMBRE NEGATIF
    *sinon :
    LE NOMBRE EST EGAL 0 ZERO 
""" 
n = 0
while n == 0 or n<3:
    try :
        nbre = int(input("saisir un nombre : "))
    
    except :
        print("ERREUR  : veuiller saisir un nombre entier ,sinon vous risquer de bloquer le programme  \n")
        nbre = int(input("saisir un nombre a nouveau : "))
    if nbre > 0 :
        print("NOMBRE POSITIF")
    elif nbre < 0 :
        print("NOMBRE NEGATIF")
    else :
        print("NOMBRE NUL")
    n=n+1