""" EXERCICE 8: DEVINER UN NOMBRE
crée une variable contenant un nombre secret (par exemple nbre_secret = 20).
utilise une boucle pour demander un nombre jusqu'a ce que l'utilisateur trouve.
à chaque tentative :
-si le nombre est trop petit, affiche "plus grand".
-s'il est trop grand affiche "plus petit"
-sinon, affiche "bravo !". 
""" 
nbre_secret = 20 
nbre =""
n = 1
while nbre != str(nbre_secret) :
    nbre =input("entrer un nombre : ")
    if nbre < str(20) :
        print("plus grand")
    elif nbre > str(20) :
        print("plus petit")
    else :
        print("bravo !")