import tkinter as tk

def afficher_informations():
    # Cacher le bouton "Afficher Informations"
    button_afficher.pack_forget()

    # Afficher les informations dans la fenêtre
    for i, info in enumerate(informations):
        label_info = tk.Label(fenetre, text=info, fg=fg_color, bg=bg_color, font=('Arial', 12, 'bold'))
        label_info.place(x=20, y=120 + i * 40)

    # Afficher le bouton "Retour"
    button_retour.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

def quitter_interface():
    # Fermer l'interface
    fenetre.destroy()

fenetre = tk.Tk()
fenetre.title("Informations")
fenetre.geometry("600x500")
bg_color = "#FFA500"  # Couleur de fond de la fenêtre (Orange)
fg_color = "#FFFFFF"  # Couleur du texte des sous-titres (Blanc)
fenetre.config(background=bg_color)

# Informations à afficher
informations = [
    "Bienvenue dans notre application d'inscription !",
    "Inscrivez-vous dès maintenant pour profiter de nos services.",
    "Veuillez remplir tous les champs pour valider votre inscription.",
    "Si vouz avez déja inscrit, veuillez remplir le champ de validation, ",
    "Consultez notre site web pour plus d'informations.",
    "Merci de votre confiance !"
]

# Titre
titre = tk.Label(fenetre, text='Informations', fg="white", bg=bg_color, font=('Arial', 24, 'bold'))
titre.pack(fill=tk.X, padx=20, pady=20)

# Bouton "Afficher Informations"
button_afficher = tk.Button(fenetre, text="Afficher Informations", command=afficher_informations, bg=bg_color, fg="white", font=('Arial', 14))
button_afficher.pack(pady=30)

# Bouton "Retour"
button_retour = tk.Button(fenetre, text="← Retour", command=quitter_interface, bg=bg_color, fg="white", font=('Arial', 12), relief=tk.RAISED)
button_retour.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

fenetre.mainloop()
