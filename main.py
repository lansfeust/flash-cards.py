""" 
Titre : flash-Cards
Nom du projet : flash-Cards

Nom du fichier : NAME

Date de la dernière révision : 05/07/2026
Date de l'avant dernière révision : 04/07/2026

Auteur(s) : EGO
Révision N°: Version 0.1
Client : maison

#-------------------------------------------------
name='Package_name',
    version='Version 0.7 ',
    packages=PackageList,PackageDirs
    url='Aucun',
    license='Libre',
    author='EGO',
    author_email='lansfeust@hotmail.fr',
    description=' Les flash cards sont des cartes d'apprentissage avec une question ou un mot d'un côté et une
réponse ou une définition de l'autre. Elles sont utilisées pour mémoriser et creation_cardsr des
informations efficacement, favorisant la répétition espacée et la consolidation du savoir. (v1 chatgpt)'

#-------------------------------------------------

Fichiers du projet :
    - main
    - base_Tk
    - FlashcardManager
    - fenetre
    - page_accueil
    - _______
    - _______

 """ 
################################################
#                Programme principal
################################################

# -----------------------------------------------
#            Zone des 'imports' de modules
# -----------------------------------------------
 
from time import sleep
from database import connect_db
from marque_page import class_marque_page


# ----------------------------------------------------
#        Zone de déclaration des variables globales
# ----------------------------------------------------
connection_db = connect_db()
marque_page = class_marque_page()

# -------------------------------------------------------
#        Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------


# -------------------------------------------------------
#                        PROGRAMME                        
# -------------------------------------------------------


if __name__ == "__main__":
    while True :
        
        if marque_page.valeur == 0 :

            import terminal_acceuil
            terminal_acceuil.terminal_acceuil( marque_page )

        elif marque_page.valeur == 1:

#            import terminal_acceil
            print('\n\tBRAVO ! ! ! \tFIN DE L\'APPLICATION ')#Efface-moi
            break#Efface-moi

        elif marque_page.valeur == 2:

            from terminal_page_2 import terminal_creation_cards
            
            creation_cards = terminal_creation_cards()
            ###Gestion des familles ####
            creation_cards.affichage_famille()
            creation_cards.selection_famille()
            creation_cards.confirmation_famille()

            ###Gestion de la question#####
            creation_cards.question()
            break#Efface-moi

        elif marque_page.valeur == 3:
            
            from terminal_page_3 import creation_famille
            famille = creation_famille()# Initialisation
            famille.input_famille_securiser()# insertion de la famille
            famille.confirmation()
            famille.input_famille()
            break#Efface-moi
        