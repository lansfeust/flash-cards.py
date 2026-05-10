
################################################
#                Programme principal
################################################

# -----------------------------------------------
#            Zone des 'imports' de modules
# -----------------------------------------------
import tkinter
from tkinter import ttk
from time import sleep

# ----------------------------------------------------
#        Zone de déclaration des variables globales
# ----------------------------------------------------
fenetre_principal = tkinter.Tk()


# -------------------------------------------------------
#        Zone de déclaration des modules ou des fonctions
# -------------------------------------------------------

class Gestionnaire_fenetre(tkinter.Tk) :

    def __init__(self , fenetre ):
        self.fenetre = fenetre
#        super().__init__()
        fenetre.title("Fenêtre principal")
        fenetre.geometry("777x1024")
 
#        self.fond_image = tkinter.PhotoImage(file="img\\Gemini_Generated_Image_6mdy1r6mdy1r6mdy.png")
#        fond_label = tkinter.Label( self.fenetre, image=self.fond_image)
#        fond_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        from page_acceil import page_acceil
        var = page_acceil( self.fenetre )
        pass

    def page_acceil(self):
        from page_acceil import page_acceil
        var = page_acceil( self.fenetre )
        
    def page_1(self):
        from page_1 import page_1
        var = page_1( self.fenetre )

    def page_2(self):
        from page_2 import page_2
        var = page_2( self.fenetre )

    def executer(self):
        self.fenetre.mainloop()

# -------------------------------------------------------
#                        PROGRAMME
# -------------------------------------------------------


if __name__ == "__main__":
    fenetre = Gestionnaire_fenetre( fenetre_principal )

    fenetre.executer()
 #   fenetre_principal.mainloop()

sleep( 2 )