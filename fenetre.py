import tkinter
from tkinter import ttk

class GestionnaireFenetre(tkinter.Tk):
    """Gère la fenêtre principale et les pages de l'application."""

    def __init__(self):
        super().__init__()  # Initialise la fenêtre Tkinter
        self._configurer_fenetre()
        self.charger_page_accueil()  # Charge la page d'accueil par défaut
        self.aff_ligne()

    def _configurer_fenetre(self):
        """Configure la fenêtre principale."""
        self.title("Fenêtre principale")
        self.geometry("777x1024")

    def aff_ligne(self):
        import tkinter as tk
                
        # Active le redimensionnement des lignes/colonnes
        for i in range(10):  # Exemple : 10 lignes
            self.grid_rowconfigure(i, weight=1)
        for i in range(5):   # Exemple : 5 colonnes
            self.grid_columnconfigure(i, weight=1)

        # Affiche les bordures des cellules
        for row in range(10):
            for col in range(5):
                frame = tk.Frame(self, borderwidth=1, relief="solid", bg="lightgray")
                frame.grid(row=row, column=col, sticky="nsew")
                tk.Label(frame, text=f"R{row},C{col}").pack()

        # Ton widget existant
        listbox = tk.Listbox(self)
        listbox.grid(row=5, column=0, columnspan=2, sticky="nsew")

    def charger_page_accueil(self):
        """Charge la page d'accueil."""
        from page_accueil import PageAccueil  # Module renommé (correction de la faute)
        PageAccueil(self)  # `self` est la fenêtre Tkinter

    def charger_page_1(self):
        """Charge la page 1."""
        from page_1 import Page1
        Page1(self)

    def charger_page_2(self):
        """Charge la page 2."""
        from page_2 import Page2
        Page2(self)

    def executer(self):
        """Lance la boucle principale de Tkinter."""
        self.mainloop()  # `self` est déjà la fenêtre

if __name__ == "__main__":
    fenetre = GestionnaireFenetre()  # Crée une instance de la fenêtre
    fenetre.executer()