from fenetre import Gestionnaire_fenetre
import tkinter

class page_acceil(Gestionnaire_fenetre) :

    def __init__(self, fenetre):
        super().__init__(fenetre)

        label9 = tkinter.Label(self.fenetre, text="bouton d'affichage page 1")
        bouton1 = tkinter.Button(text='premier bouton',textvariable='premier bouton',padx=15,command=lambda:self.page_1() )
        bouton1.grid(row=4, column=0, sticky="w")
        
        pass