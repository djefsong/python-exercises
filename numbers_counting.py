""" EXERCICE 7: COMPTEUR  
Demande a l'utilisateur un nombre positif.
avec une boucle :
-compte de 0 jusqu'a ce nombre ;
-puis de ce nombre jusqu'a 0 """
nombre = ""
n = 0 
nombre = input("entrer un nombre : ") 
while  n <= int(nombre) :
    print(n)
    n = n + 1 
while  int(nombre) > 0 :
        nombre = int(nombre) - 1
        print (nombre)