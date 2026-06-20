import tkinter
from fenetre import GestionnaireFenetre

class Page1:
    def __init__(self, parent: tkinter.Tk):
        self.parent = parent

        # Efface les widgets précédents (optionnel, pour éviter les superpositions)
        for widget in self.parent.winfo_children():
            widget.destroy()

        # Utilise grid() pour tous les widgets
        label = tkinter.Label(self.parent, text="Page 1")
        label.grid(row=0, column=0, padx=10, pady=10)  # ✅ grid()

        bouton_retour = tkinter.Button(
            self.parent,
            text="Retour à l'accueil",
            command=lambda: self.parent.charger_page_accueil()
        )
        bouton_retour.grid(row=1, column=0, padx=10, pady=10)  # ✅ grid()