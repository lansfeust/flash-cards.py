""" 
Titre : flash-Cards
Nom du projet : flash-Cards

Nom du fichier : NAME

Date de la dernière révision : 20/06/2026

Auteur(s) : EGO
Révision N°: Version 0.1
Client : maison

#-------------------------------------------------
name='Package_name',
    version='Version 0.6 ',
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
from fenetre import GestionnaireFenetre 
from database import connect_db , create_table


# ----------------------------------------------------
#        Zone de déclaration des variables globales
# ----------------------------------------------------
connection_db = connect_db()

# -------------------------------------------------------
#        Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------
## Création des tables ( Si elle n'existe pas )
create_table( connection_db )

# -------------------------------------------------------
#                        PROGRAMME                        
# -------------------------------------------------------


if __name__ == "__main__":
    fenetre = GestionnaireFenetre()
    
    fenetre.executer()
sleep( 2 )