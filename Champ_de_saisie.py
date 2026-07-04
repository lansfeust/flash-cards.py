  """
        Crée :
        - Un menu déroulant pré-rempli (catégories).
        - Un champ "Questions".
        - Un champ "Réponses".
        - Un bouton "Valider" pour traiter les 3 formulaires.
        """
        # 1️⃣ Menu déroulant (pré-rempli)
        tkinter.Label(self.parent, text="Catégorie :").grid(row=0, column=0, padx=5, pady=5)
        self.categorie_var = tkinter.StringVar()  # Variable pour stocker la sélection
        self.combo_categorie = ttk.Combobox(
            self.parent,
            textvariable=self.categorie_var,
            values=["Famille", "Amis"  , "Travail", "Autre"]  # Options pré-remplies
        )
        self.combo_categorie.grid(row=0, column=1, padx=5, pady=5)
        self.combo_categorie.current(0)  # Sélectionne "Famille" par défaut

        # 2️⃣ Champ "Questions"
        tkinter.Label(self.parent, text="Questions :").grid(row=1, column=0, padx=5, pady=5)
        self.entry_Questions = tkinter.Entry(self.parent, width=30)
        self.entry_Questions.grid(row=1, column=1, padx=5, pady=5)

        # 3️⃣ Champ "Réponses"
        tkinter.Label(self.parent, text="Réponses :").grid(row=2, column=0, padx=5, pady=5)
        self.entry_Reponses = tkinter.Entry(self.parent, width=30)
        self.entry_Reponses.grid(row=2, column=1, padx=5, pady=5)

        # 4️⃣ Bouton "Valider" (traite les 3 formulaires)
        tkinter.Button(
            self.parent,
            text="Valider",
            command=lambda: self.valider_formulaires  # Appelle la méthode ci-dessous
        ).grid(row=5, column=0, columnspan=2, pady=5)