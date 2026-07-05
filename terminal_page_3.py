################################################
#				Programme principal
################################################

# -----------------------------------------------
#		    Zone des 'imports' de modules
# -----------------------------------------------
from database import connect_db , insert_famille , get_famille
from fonction_perso import confirmation

# ----------------------------------------------------
#		Zone de déclaration des variables globales
# ----------------------------------------------------


# -------------------------------------------------------
#		Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------


class creation_famille :

    def __init__(self):
        self.connection = connect_db()# connection a la base de donné 
        self.famille = get_famille( self.connection )#Extraction des familles
        pass

    def input_famille(self):
        """
            Sauvegarde de la famille dans la base de donnée
        """
        insert_famille(self.connection , self.famille_choisi )
        pass

    def affichage_famille(self):
        print('-'*49)#Choix estetique
                
        print('\nListe de toutes les familles\n')

        variable_temporaire = []# Utiliser pour effacer l'ID de self.famille 
        for id_famille , famille in self.famille :
            
            print(famille)# affiche toutes les familles existante
            variable_temporaire.append(famille)
        
        self.famille_sans_id = variable_temporaire # Efface les ID 

        print('\n')

    def ecriture_famille_securiser(self,message_erreur=None):
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
        
        self.affichage_famille()

        if message_erreur :
            print(message_erreur)

        non_temporaire = input('\nQuel famille voulez-vous crée ?\n')

        for verification in non_temporaire :
            if verification in caracteres_interdis :
                message_erreur='caracteres interdis !\tUniquement des lettres !'
                self.ecriture_famille_securiser(message_erreur)
                break
            
        if len( non_temporaire )  < 3 :
            message_erreur='le nom est trop court '
            self.ecriture_famille_securiser(message_erreur)
        elif len(non_temporaire) > 15 :
            message_erreur='le nom est trop long'
            self.ecriture_famille_securiser(message_erreur)
        elif non_temporaire is int :
            message_erreur='la famille ne peut pas etre un nombre '
            self.ecriture_famille_securiser(message_erreur)
        else :
            self.nom = non_temporaire
            self.famille_choisi = non_temporaire #deuxiéme version ( a choisir plus tard )

    def confirmation(self):

        question = '\n\tEtes vous sûr de vouloir crée la famille "',self.nom,'" ? \n\n'
        retour = confirmation(self.famille_choisi , None , self.famille_sans_id )

        if retour == False :
            self.ecriture_famille_securiser()

    def old_confirmation(self):
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
            
    from terminal_page_3 import creation_famille

    teste = creation_famille()# Initialisation
    teste.ecriture_famille_securiser()# insertion de la famille
    teste.confirmation()
    teste.input_famille()


