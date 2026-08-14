''' EXERCICE 2: Pair ou impair 
Demande à l' utilisateur de saisir un nombre.
- Si le nombre est pair , affiche "Le nombre est pair".
- Sinon, affiche "Le nombre est impair"
'''

nombre = ""
diviseur = 2

while not nombre == " 0 " :
    nombre =input("saisir un nombre : " )
        
    resultat = int(nombre) % diviseur
            
    if resultat == 0 :
        print("le nombre est pair \n")
    else : 
        print("le nombre est impair \n")