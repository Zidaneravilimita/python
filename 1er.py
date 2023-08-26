import tkinter as tk
import sqlite3
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk

dev = tk.Tk()
dev.title("Informations")
dev.geometry("900x500")
dev.config(background="#FFFFFF")  # Couleur de fond de la fenêtre principale

#image de fond
image = Image.open("font.png")
photo = ImageTk.PhotoImage(image)

background_label = tk.Label(dev, image=photo)
background_label.place(x=100, y=0)

def valider_formulaire():
    nom = nom_entry.get()
    mdp = mdp_entry.get()

    # Connexion à la base de données
    conn = sqlite3.connect("test_Python.db")
    cursor = conn.cursor()

    # Vérification de l'utilisateur existant
    cursor.execute("SELECT * FROM utilisateurs WHERE nom=? AND mdp=?", (nom, mdp))
    utilisateur = cursor.fetchone()
    if utilisateur:
        messagebox.showinfo("Validation réussie", "Utilisateur valide")
        ouvrir_interface_utilisateur()
    else:
        messagebox.showerror("Erreur de validation", "Nom ou mot de passe incorrect")

    # Fermeture de la connexion
    conn.close()

def ouvrir_interface_utilisateur():
    # Code pour ouvrir l'interface de l'utilisateur validé
    subprocess.call(["python", "interface_utilisateur.py"])

def reset():
    nom_entry.delete(0, tk.END)
    mdp_entry.delete(0, tk.END)

#fonction pour sign up
def ouvre():
    subprocess.call(["python", "zidane.py"])

# Titre
titre_label = tk.Label(dev, text="Sign In", font=("Arial", 24, "bold"), bg="#FFFFFF", fg="#FFA500")
titre_label.place(x=645, y=18)

# Champ Nom
nom_frame = tk.Frame(dev, bg="#FFFFFF")
nom_frame.place(x=510, y=80)
nom_label = tk.Label(nom_frame, text="Nom:", font=("Arial", 14), bg="#FFFFFF", fg="#000000", padx=10)
nom_label.pack(side=tk.LEFT)
nom_entry = tk.Entry(nom_frame, font=("Arial", 12), width=30)
nom_entry.pack(side=tk.LEFT)

# Champ Mot de passe
mdp_frame = tk.Frame(dev, bg="#FFFFFF")
mdp_frame.place(x=500 ,y=130)
mdp_label = tk.Label(mdp_frame, text="Mot de passe:", font=("Arial", 14), bg="#FFFFFF", fg="#000000", padx=10)
mdp_label.pack(side=tk.LEFT)
mdp_entry = tk.Entry(mdp_frame, font=("Arial", 12), show="*", width=25)  # Utilisation de show="*" pour masquer les caractères
mdp_entry.pack(side=tk.LEFT)

# Bouton Valider
valider_button = tk.Button(dev, text="Valider", font=("Arial", 12), width=25, bg='#1752D4', command=valider_formulaire)
valider_button.place(x=570, y=200)

# Bouton Reset
button_reset = tk.Button(dev, text="Reset", font=("Arial", 12), bg='#58424E', command=reset)
button_reset.place(x=666, y=250)

#titre en bas
titre_bas = tk.Label(dev, text="Créer un compte ?", font=("Arial", 9), bg="#FFFFFF")
titre_bas.place(x=600, y=285)

#titre en bas
titre_bas2 = tk.Button(dev, text="Sign Up", font=("Arial", 9), bg="#FFFFFF", fg='#1799D4', command = ouvre)
titre_bas2.place(x=710, y=285)


dev.mainloop()
