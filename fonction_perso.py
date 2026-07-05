def confirmation(depart , si_oui , si_non):
    print('-'*49)#Choix estetique
    
    while True:
        print('\nVoici votre choix voulez-vous la concervé ?\n\n', depart)#Affiche le choix de l'utilisateur
        choix = input('\nConservé ? oui , non \n\t')
        
        liste_autorisé = ('o',
                            'O',
                            'y',
                            'yes',
                            'oui')#Liste des actions qui veux dire 'OUI'
        
        if choix in liste_autorisé :#Si oui on quitte la fonction et passe a la suite du script
            return True
            break

        elif choix == 'n' or choix == 'non' or choix == 'no':# Si non , on re-pose la question

            if type(si_non) is list :#petit scrypt qui debogue si c'est une liste

                for liste in si_non :
                    print( liste )
                depart = input( ' ' )

            else:
                non = """\n {0}\n""".format(str(si_non))
                depart = input( non )
            
            return False
        elif choix =='q' or choix == 'quit' :
            exit()

        else:# Si l'utilisateur ne rentre ni oui ni non , on recomance depuit le debut
            continue

if __name__ == '__main__':
    print('-'*(7*7))