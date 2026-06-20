import tkinter

class PageAccueil:
    """Classe représentant la page d'accueil de l'application."""

    def __init__(self, parent: tkinter.Tk):
        self.parent = parent  # `parent` est la fenêtre Tkinter (instance de `GestionnaireFenetre`)

        # Label d'affichage
        label9 = tkinter.Label(
            self.parent,
            text="Bouton d'affichage page 1"
        )
        label9.grid(row=3, column=0, sticky="w")

        # Bouton pour charger la page 1
        bouton1 = tkinter.Button(
            self.parent,
            text="Premier bouton",
            padx=15,
            command=lambda: self.parent.charger_page_1()  # Appelle la méthode du parent
        )
        bouton1.grid(row=4, column=0, sticky="w")