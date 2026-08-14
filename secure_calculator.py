""" EXERCICE 4: CALCULATRICE SECURISEE
Demande deux nombres à l' utilisateur avec try/except.
Ensuite, demande une operation ( +,-,* ou /).
Affiche le resultat.
Si l'utilisateur  saisit autre chose qu'un nombre, affiche un message d'erreur sans que le programme plante 
"""



a = int
b = int 
operat_arithmq = ""
n=1
# tant que l operateur n entre pas des nombres entier il recoit deux exceptions où le programme lui redemande de saisir les nombres , mais apres deux exceptions echouer le programme bug et s'arrete   
while not operat_arithmq == "+" or "-" or "*" or "/"  :
    try :
        a = int(input(" veiller entrer un entier a : "))
        b = int(input(" veiller entrer un entier b : "))
        print("")
    except :
        print("ERREUR: Veuiller saisir uniquement des nombres entiers <(^_^)> \n")

        try :
            a = int(input(" veiller entrer un entier a : "))
            b = int(input(" veiller entrer un entier b : "))
            print("")
            print("faire une operation avec a et b ")
        except :
    
            print("ERREUR: ATTENTION VOUS RISQUEZ DE BLOQUER LE PROGRAMME/","Veuiller saisir uniquement des nombres entiers! <(-_-)>  \n")
            a = int(input(" veiller entrer un entier a : "))
            b = int(input(" veiller entrer un entier b : "))
            print("")
            print("faire une operation avec a et b ")
    else :
# si l utilsateur entre uniquement des entiers apres la premiere ou deuxiemme exception alors le programme continue 
        print("faire un operation de calcul avec a et b \n")

    operat_arithmq  = input("entrer  un operateur arithmetique  (+, -, *, /): " )

    if operat_arithmq == "+" :
        print ("result = "+str(a+b))

    elif operat_arithmq == "-" :
        print("result = "+str(a-b))

    elif operat_arithmq == "*" :
        print("result = "+str(a*b))

    elif operat_arithmq == "/" :
        while a == 0 :
            print("ERREUR : operation impossible")
            operat_arithmq  = input("entrer un operateur arithmetique  (+, -, *, /): " )
            if operat_arithmq == "/" :
                print("result = "+str(a/b))
            else :
                print("operation invalide")
            n=n+1 
        else :
            print("result = "+str(a/b))
    n=1 