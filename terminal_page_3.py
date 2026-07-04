################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------
from database import connect_db , insert_famille

# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------


# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------


class creation_famille :

    def __init__(self):
        pass

    def input_famille(self):
        self.connection = connect_db()# connection a la base de donné 
        insert_famille(self.connection , self.nom )
        pass

    def input_famille_securiser(self):
        caracteres_interdis = (' ',
                               ',',
                               '?',
                               ';',
                               '.',
                               ':',
                               '/',
                               '\\',
                               '!',
                               '§',
                               '%',
                               '@',
                               '#',
                               '"',
                               '&',
                               '{',
                               '}',
                               '[',
                               ']',
                               '|',
                               '_',
                               '*',
                               '+',
                               '=',)
        non_temporaire = input('Quel famille voulez-vous crée ?\n')

        if len( non_temporaire )  < 3 :
            print('le nom est trop court ')
        elif len(non_temporaire) > 15 :
            print('le nom est trop long')
        elif non_temporaire is int :
            print('la famille ne peut pas etre un nombre ')
        elif non_temporaire in caracteres_interdis :
            print('caracteres interdis !\tUniquement des lettres !')
        else :
            self.nom = non_temporaire
    def confirmation(self):
        print('\n\tEtes vous sûr de vouloir crée la famille ',self.nom,' ? \n\n')
        confirmation = input("Ecrivez 'y' ou 'o' pour confirmé ou 'n' pour annulé et 'q' pour quitter")

        while True :
            if confirmation == 'y' or 'yes' or 'oui' or 'o' :
                break
            elif  confirmation == 'n' or 'no' or 'non' : 
                self.input_famille_securiser()
            elif  confirmation == 'q' : 
                exit()
            else :     
                print('\n\tEtes vous sûr de vouloir crée la famille ',self.nom,' ? \n\n ')
                confirmation = input("Ecrivez 'y' ou 'o' pour confirmé ou 'o' et 'n' pour annulé ")
# -------------------------------------------------------
#						PROGRAMME
# -------------------------------------------------------



if __name__ == "__main__" :
    _______
    pass







