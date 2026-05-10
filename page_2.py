from fenetre import Gestionnaire_fenetre
import tkinter

class page_2(Gestionnaire_fenetre) :

    def __init__(self, fenetre):
        super().__init__(fenetre)
        
        self.fenetre.title("Fenêtre n°2 avec 3 Textareas")
        textarea1 = tkinter.Text(self.fenetre, height=5, width=30)
        textarea1.grid(row=0, column=0, padx=10, pady=10)
        # Facultatif: Ajouter des labels pour clarifier l'utilisation
        label1 = tkinter.Label(self.fenetre, text="Textarea de la page 2:")
        label1.grid(row=1, column=0, sticky="w") # "w" pour aligner à gauche
        
        label9 = tkinter.Label(self.fenetre, text="bouton d'affichage page 1")
        bouton1 = tkinter.Button(text='premier bouton',textvariable='premier bouton',padx=15,command=lambda:self.page_1() )
        bouton1.grid(row=4, column=0, sticky="w")

        pass

