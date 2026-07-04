################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------
from database import create_table , connect_db

# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------

list_de_choix = """
\nacceuil\t=>\t0
teste de cards\t=>\t1
création de cards\t=>\t2
création de famille\t=>\t3
"""

# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

def terminal_acceuil( marque_page ):
    
    while True :
        choix = input(list_de_choix + 'Quel page affiché ?\tchoisiser un nombre\n\n')

        #########Teste le choix de l'utilisateur , si le teste est bon , on passe a la suite #########
        try :
            choix = int(choix)
            if choix >= 0 and choix < 4 :# Si le choix et dans la liste ...
                print('if choix')
                break
        except :
            continue


    ## Création des tables ( Si elle n'existe pas )
    bdd = connect_db()
    create_table( bdd )

    ## mise a jour de marque_page
    marque_page.valeur = choix
    print('marque_page.valeur\t',marque_page.valeur)
    return None


# -------------------------------------------------------
#						PROGRAMME
# -------------------------------------------------------

if __name__ == "__main__" :
    _______







