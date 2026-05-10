""" 
Titre : flash-Cards
Nom du projet : flash-Cards

Nom du fichier : NAME

Date de la dernière révision : 07/05/2026

Auteur(s) : EGO
Révision N°: Version 0.1
Client : maison

#-------------------------------------------------
name='Package_name',
    version='Version 0.5 ',
    packages=PackageList,PackageDirs
    url='Aucun',
    license='Libre',
    author='EGO',
    author_email='lansfeust@hotmail.fr',
    description=' Les flash cards sont des cartes d'apprentissage avec une question ou un mot d'un côté et une
réponse ou une définition de l'autre. Elles sont utilisées pour mémoriser et tester des
informations efficacement, favorisant la répétition espacée et la consolidation du savoir. (v1 chatgpt)'

#-------------------------------------------------

Fichiers du projet :
    - main
    - base_Tk
    - FlashcardManager
    - _______
    - _______
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
from fenetre import Gestionnaire_fenetre , fenetre_principal


# ----------------------------------------------------
#        Zone de déclaration des variables globales
# ----------------------------------------------------

# -------------------------------------------------------
#        Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

# -------------------------------------------------------
#                        PROGRAMME                        
# -------------------------------------------------------


if __name__ == "__main__":
    fenetre = Gestionnaire_fenetre( fenetre_principal )



    fenetre.executer()
sleep( 2 )