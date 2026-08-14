''' EXERCICE 3: Mot de passe 
Crée une variable contenant le mot de passe : python123.
Demande a l'utilisateur de saisir un mot de passe.
*L'utilisateur a droit a 3 essais 
*Si le mot de passe est correct, affiche "Connexion reussie".
*Sinon, affiche "Mot de passe incorret" et si les 3 essais sont epuisés affiche "compte bloqué".

'''
mdp = ""
n = 0
while not mdp =="python123" and n < 3  :
    mdp = input("saisir un mot de passe : ")
    n = n + 1
    if mdp == "python123" :
        print("mot de passe correct\n","vous avez reussie (^_^)") 
    elif mdp != "python123" :
        print("mot de passe incorrect ('_') \n")
    if n == 2 :
        print("Attention vous risquez de bloqué votre compte si vous echouer a nouveau 'le mot de passe !' ")
while n == 3 and mdp !="python123" :
    print("compte bloqué (-_-)")

    n = n + 1