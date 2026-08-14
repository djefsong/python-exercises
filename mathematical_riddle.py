""" EXERCICE 9: DEVINETTE MATHEMATIQUE 
L'ordinateur demande combien font : 8 x 7 ?
-Tant que la reponse est fausse, repose la question.
-à la fin, affiche le nombre d'essais effectués avant de trouver la bonne reponse.
"""
reponse = 56 
n = 0
calcul = ""
while calcul != str(reponse) :
    calcul = input("combien font 8 x 7 = ")
    if calcul == str(reponse) :
        print("juste") 
    else : 
        print("faux")     
    n = n + 1
print("vous avez essayer " + str(n) +" fois " + "avant de trouver la bonne reponse ")