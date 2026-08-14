"""LE BANQUIER
Le compte bancaire contient 20 000 fcfa.
L'utilisateur saisir un montant a retirer.
-Si le montant est superieur au solde, affiche "Fonds insuffisants.".
-Sinon, effectue le retrait et affiche le nouveau solde.
Le programme continue jusqu'a ce que le solde atteigne 0 fcfa. 
""" 
solde_compte = 20000
while solde_compte > 0 :
    montant_a_retirer=int(input("montant a retirer : "))
    if montant_a_retirer > solde_compte :
        print("Fonds insuffisants.")
    else :
        solde_compte = solde_compte - montant_a_retirer
        print("Nouveau solde : " + str(solde_compte) +" FCFA")
        #print(f"Nouveau solde : {solde_compte} FCFA")
print("Solde à 0 FCFA. Fin du programme.") 