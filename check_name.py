''' EXERCICE 5: VERIFICATION NOM ET PRENOM
demander a l'utilisateur d'entrer son nom et son prenom.
*il a le choix entre son premier et son deuxieme nom;
*puis il a le choix entre son premier et son deuxieme prenom.

en  utilisant la boucle while tant que un des noms  ou prenoms est different de :
nom=(lotse et pieben ), prenom=(djef et gastril) le programme redemandera d entrer son nom 
et son prenom jusqu'a ce que ceux ci soient justes.

*si nom et prenom correct : afficher "NOM ET PRENOMS VALIDES"
*sinon : afficher "NOM ET PRENOMS ERRONER"
'''
nom = None
prenom = None
n = 1
while   (nom != "lotse" and nom !="pieben" or prenom != "djef" and prenom != "gastril")   : 
    nom = input("quel est ton nom : ") 
    prenom = input("quel est ton prenom : ")
    print("")

    if nom != "lotse" and nom !="pieben" or prenom != "djef" and prenom != "gastril" :
        print("ERREUR : NOM ET PRENOM ERRONER  <(°_°)> n")
        print("Veillez réessayer\n")

    else:
        print("NOM OU PRENOM VALIDES :  <(^_^)> ")
    n=1
