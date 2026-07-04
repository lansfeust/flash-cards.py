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


# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

class terminal_creation_cards:

    def __init__(self):
        pass

    def affichage_famille(self):
        self.connection = connect_db()
        self.famille = get_famille( self.connection )#Extraction des familles

        temps_nombre_famille = get_nombre_famille( self.connection )#Version temporaire (une liste dans une liste)
        self.nombre_famille = int(temps_nombre_famille[0][0])#nombre extraite correctement
        
        print('\nListe de toutes les familles\n')
        for famille , id_famille in self.famille :
            print(famille,'\t=>\t',id_famille)# affiche toutes les familles et le numéros qui correspond 
        print('\n')

    def selection_famille(self):

        while True :
            id_famille = input('veuillez séléctionner une famille\n')# l'utilisateur donne l'ID de la famille choisi
            try :# Teste si l'utilisateur ne c'est pas trompé 
                id_famille = int( id_famille )
            except :
                self.affichage_famille()
                continue
            
            if id_famille == 0 or id_famille > self.nombre_famille :# Si le nombre est trop grand ou == zero
                continue
            else :
                break
            
        self.famille_choisi = id_famille

    def confirmation_famille(self):
        while True :
            print('êtes-vous sur de choisir ',self.famille_choisi,'?\n')
            choix = input("'o' pour confirmé 'n' pour recomancé 'q' pour quitté\n")

            liste_de_choix = ('o',
                'O',
                'y',
                'yes',
                'oui',)

            if choix in liste_de_choix :
                break
            elif choix =='n':

                self.affichage_famille()
                self.selection_famille()
                continue

            elif choix =='q' or choix == 'quit' :
                exit()
            else :
                continue 

# -------------------------------------------------------
#						PROGRAMME
# -------------------------------------------------------

if __name__ == "__main__" :
    teste = terminal_creation_cards()
    ###Gestion des familles ####
    teste.affichage_famille()
    teste.selection_famille()
    teste.confirmation_famille()

    ###estion de la question#####







