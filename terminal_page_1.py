################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------
from database import *

# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------
#_______ = _______

# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

class utilisation_flashCards():

    def __init__(self):
        self.connection = connect_db()
        pass

    def selection_aleatoire(self):
        liste_cards = get_all_flashcards( self.connection )
        for liste in liste_cards :
            print(liste)


# -------------------------------------------------------
#						PROGRAMME
# -------------------------------------------------------

if __name__ == "__main__" :
    teste = utilisation_flashCards()
    teste.selection_aleatoire()

    print('fin de l application')







