from tkinter import ttk  # ← Ajoute cette importation en haut de ton fichier
import tkinter
from database import connect_db, get_flashcard_by_id , get_all_ID

class Page3:
    def __init__(self, parent: tkinter.Tk):
        self.parent = parent
        self.connection = connect_db()
        self.clean()
        self.aff_all_ID()
        self.Bouton_Retour()

#        get_flashcard_by_id()
        pass
    
    def clean(self):
        """
        Supprime tous les widgets enfants de la fenêtre parente
        pour éviter les superpositions et préparer l'affichage.
        """
        for widget in self.parent.winfo_children():
            widget.destroy()

    def aff_all_ID(self):
        ##Affiche tout les id des flash-cards##
        vars = get_all_ID( self.connection )

        print('\n Nombre de flash-cards =>',vars[:-0])

    def aff_flashcards(self):
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

    def Bouton_Retour(self):
        """Ajoute un bouton pour revenir à la page d'accueil."""
        tkinter.Button(
            self.parent,
            text="Retour a l'acceuil",
            command=lambda: self.parent.charger_page_accueil()
        ).grid(row=3, column=0, columnspan=2, pady=5)
    pass

    get_flashcard_by_id