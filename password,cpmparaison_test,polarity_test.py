''' EXERCICE 1: partie 1/coffre fort  
Ecrire un programme qui fonctionne ainsi :
    1. Le programme demande à l'utilisateur de saisir un mot de passe.
    2. Le mot de passe correct est : python2026.
    3. L'utilisateur a 3 essais maximum.
    4. si le mot de passe est correct :
        * afficher "ouverture du coffre!"
        * arreter la boucle.
    5. Si le mot de passe est faux :
        *afficher "Mot de passe incorrect."
        *afficher le nombre d essais restants.
    6. si les 3 essais sont utilisés :
        *au denier essaie : prevenir a l'utilisateur que le coffre va etre bloque et une alarme va se declancher s'il echoue le mot de passe
        *afficher "coffre bloqué."
'''

mot_de_passe = ""
n = 0
m = 3
i = 3
print("essaies restant :"+ str(m)+"/3")
while not mot_de_passe == "python2026" and n < 3 :
    
    mot_de_passe = input("entrer un mot de passe ")
    n = n + 1
    i=i-1
    if mot_de_passe == "python2026" :
        print("ouverture du coffre! (^_^)")
    elif not mot_de_passe == " python2026 " :
        print("")
        print("mot de passe incorrect.\n")
        print("il vous reste :"+ str(i)+"/3 essais ")
        if i < 2 :
           print("attention vous allez bloquer le coffre et declancher l'alarme si vous echouer a nouveau le mot de passe")    
    else :
     
        print("essaie restant :0/3")
        if i == 0 :
            print("")
            print("coffre bloqué! (°_°)") 
            print("ALARME!!! ALARME!!! ALARME!!!")

""" EXERCICE 1: partie 2
Apres la connexion reusie :
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