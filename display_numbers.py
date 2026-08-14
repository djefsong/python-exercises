

''' EXERCICE 1: partie 3
à l'aide d'une boucle for, affiche tous les nombres de 1 jusqu'au nombre saisi.
ex: si l'utilisateur saisir 4, le programme doit afficher :
1
2
3
4
''' 
nbre = input("entrer un nombre entier ")
for nombre in nbre :
    n= 1
    while  n <= int(nombre) :
        print(n)
        n += 1 