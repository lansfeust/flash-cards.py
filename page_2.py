import tkinter
from database import connect_db, insert_famille

class Page2:
    def __init__(self, parent: tkinter.Tk):
        self.parent = parent
        self.connection = connect_db()
        self.clean() # Efface les widgets précédents
        self.Champ_de_saisie()
        self.Bouton_Retour()
        self.decoration()
        
    def clean(self) :# Efface les widgets précédents
        for widget in self.parent.winfo_children():
            widget.destroy()

    def Champ_de_saisie(self):
        tkinter.Label(self.parent, text="Nom de la famille :").grid(row=0, column=1, padx=5, pady=5)
        entry_nom = tkinter.Entry(self.parent, width=30)
        entry_nom.grid(row=1, column=1, padx=5, pady=5)
        
        tkinter.Button(
            self.parent,
            text="Valider",
            command=lambda: insert_famille(self.connection, entry_nom.get())
        ).grid(row=2, column=0, columnspan=2, pady=5)

    def Bouton_Retour(self):
        tkinter.Button(
            self.parent,
            text="Retour a l'acceuil",
            command=lambda: self.parent.charger_page_accueil()
        ).grid(row=3, column=0, columnspan=2, pady=5)

    def decoration(self)    :
        self.parent.geometry("800x600")  # Largeur x Hauteur
        self.parent.title("Gestion des familles")
