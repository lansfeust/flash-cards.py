from tkinter import ttk  # ← Ajoute cette importation en haut de ton fichier
import tkinter
from database import connect_db, insert_famille, get_famille , insert_flashcard

class Page1:
    def __init__(self, parent: tkinter.Tk):
        """
        Initialise la page de gestion des cards.
        - Nettoie les widgets existants,
        - Crée les champs de saisie et boutons,
        - Configure la fenêtre,
        """
        self.parent = parent
        self.connection = connect_db()
#        self.aff_famille()
        self.clean()  # Efface les widgets précédents
        self.decoration()
#        self.Champ_de_saisie()
        self.terminal_Champ_de_saisie()
        self.Bouton_Retour()

    def terminal_Champ_de_saisie(self):
        ##Affichage des famille dans un pseudo menue déroulant##
        variable = get_famille(self.connection)
        for ligne in variable :
            print('ID=>\t',ligne[0],'\t',ligne[1] )

        #Création d'une flash-Cards
#        print("Séléctionné l'id d'une famille\n")
        temps_famille = input("Séléctionné l'id d'une famille\n")
        temps_question = input("Ecrivé la question\n")
        temps_reponse = input("Ecrivé la réponse\n")
        
        self.terminal_verification_formulaire(temps_famille , temps_question , temps_reponse)

        print('\n',temps_famille,temps_question,temps_reponse)#Efface-moi
        print(len(temps_question))#Efface-moi
        
        insert_flashcard(self.connection, temps_question, temps_reponse, temps_famille, 1, 'now')#Enregistrement de la flash-cards

    def clean(self):
        """
        Supprime tous les widgets enfants de la fenêtre parente
        pour éviter les superpositions et préparer l'affichage.
        """
        for widget in self.parent.winfo_children():
            widget.destroy()

    def terminal_verification_formulaire(self,famille , question , reponse ):
        """
        Fait différent teste pour verifié que l'utilisateur n'a pas commis d'erreur
        1. teste si les formulaires sont vide ou si il ne sont pas assé remplie
        2.teste si famille est bien un entier 
        """
        if None in (famille , question , reponse) :#Teste si c'est vide
            print('\n\tErreur : formulaire vide\n')
            self.terminal_Champ_de_saisie()

        elif len(question) < 3 or len(famille) > 2 :#Teste si c'est trop petit
            print('\n\tErreur : formulaire pas assez remplie\n\t')
            self.terminal_Champ_de_saisie()
            
        try :
            famille = int(famille)
        except:
            print('\n\tErreur : n est pas un nombre\n\t')
            self.terminal_Champ_de_saisie()

    def Champ_de_saisie(self):
        """
        Crée :
        - Un label et deux champs de saisie pour la question et la réponse de la card.
        - Un bouton "Valider" pour ajouter la cards en base de données.
        """
        tkinter.Label(self.parent, text="Question :").grid(row=0, column=1, padx=5, pady=5)
        entry_nom = tkinter.Entry(self.parent, width=30)
        entry_nom.grid(row=1, column=1, padx=5, pady=5)

        tkinter.Label(self.parent, text="Réponse :").grid(row=2, column=1, padx=5, pady=5)
        entry_nom = tkinter.Entry(self.parent, width=30)
        entry_nom.grid(row=1, column=3, padx=5, pady=5)

        tkinter.Button(
            self.parent,
            text="Valider",
            command=lambda: insert_famille(self.connection, entry_nom.get())
        ).grid(row=5, column=0, columnspan=2, pady=5)

    def valider_formulaires(self):
        """Récupère et traite les données des 3 formulaires."""
        categorie = self.categorie_var.get()
        question = self.entry_Questions.get()
        reponse = self.entry_Reponses.get()

        # Exemple : Affichage dans la console (à remplacer par ton appel à `insert_famille`)
        print(f"Catégorie: {categorie}, Question: {question}, Réponse: {reponse}")

        # Pour insérer en base de données (adapte selon ta fonction) :
        # insert_famille(self.connection, categorie, question, reponse)

    def Bouton_Retour(self):
        """Ajoute un bouton pour revenir à la page d'accueil."""
        tkinter.Button(
            self.parent,
            text="Retour a l'acceuil",
            command=lambda: self.parent.charger_page_accueil()
        ).grid(row=3, column=0, columnspan=2, pady=5)

    def decoration(self):
        """Configure la taille et le titre de la fenêtre."""
        self.parent.geometry("340x280")  # Largeur x Hauteur
        self.parent.title("Création d'une Flash-Cards")

    def aff_famille(self):
        """
        Affiche la liste des familles dans une Listbox avec barre de défilement.
        - Récupère les données depuis la base via `get_famille()`.
        - Insère chaque nom de famille dans la Listbox.
        """
        famille = get_famille(self.connection)

        # Liste défilable
        self.listbox = tkinter.Listbox(self.parent, width=50, height=10)
        self.listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Barre de défilement
        scrollbar = tkinter.Scrollbar(self.parent, command=self.listbox.yview)
        scrollbar.grid(row=5, column=2, sticky="ns")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Ajoute les noms des familles à la Listbox
        for ligne in famille:
            self.listbox.insert(tkinter.END, ligne[1])