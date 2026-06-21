import tkinter
from database import connect_db, insert_famille, get_famille

class Page2:
    def __init__(self, parent: tkinter.Tk):
        """
        Initialise la page de gestion des familles.
        - Nettoie les widgets existants,
        - Crée les champs de saisie et boutons,
        - Configure la fenêtre,
        - Affiche la liste des familles.
        """
        self.parent = parent
        self.connection = connect_db()
        self.clean()  # Efface les widgets précédents
        self.Champ_de_saisie()
        self.Bouton_Retour()
        self.decoration()
        self.aff_famille()

    def clean(self):
        """
        Supprime tous les widgets enfants de la fenêtre parente
        pour éviter les superpositions et préparer l'affichage.
        """
        for widget in self.parent.winfo_children():
            widget.destroy()

    def Champ_de_saisie(self):
        """
        Crée :
        - Un label et un champ de saisie pour le nom de la famille.
        - Un bouton "Valider" pour ajouter la famille en base de données.
        """
        tkinter.Label(self.parent, text="Nom de la famille :").grid(row=0, column=1, padx=5, pady=5)
        entry_nom = tkinter.Entry(self.parent, width=30)
        entry_nom.grid(row=1, column=1, padx=5, pady=5)

        tkinter.Button(
            self.parent,
            text="Valider",
            command=lambda: insert_famille(self.connection, entry_nom.get())
        ).grid(row=2, column=0, columnspan=2, pady=5)

    def Bouton_Retour(self):
        """Ajoute un bouton pour revenir à la page d'accueil."""
        tkinter.Button(
            self.parent,
            text="Retour a l'acceuil",
            command=lambda: self.parent.charger_page_accueil()
        ).grid(row=3, column=0, columnspan=2, pady=5)

    def decoration(self):
        """Configure la taille et le titre de la fenêtre."""
        self.parent.geometry("800x600")  # Largeur x Hauteur
        self.parent.title("Gestion des familles")

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


            