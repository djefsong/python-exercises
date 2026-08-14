''' EXERCICE 6: TABLE DE MULTIPLICATION
Demande un nombre a l'utilisateur.
Avec une boucle :
-affiche sa table de multiplicatiion  de 1 a 10
''' 
n = 1 
nbre =""
nbre = input("entre un nombre : ")

while n <= 10 :
    result = int(nbre) * n 
    print ( str(nbre) + "x" + str(n) + " = " + str(result))
    n = n + 1 