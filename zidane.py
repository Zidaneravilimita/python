import tkinter as tk
import subprocess
import sqlite3
import random
import io
import base64
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

def connecter():
    fenetre.destroy()
    subprocess.call(["python", "1er.py"])

def ouvrir_fenetre():
    subprocess.call(["python", "2em.py"])

def generer_mot_de_passe():
    longueur = 8  # Longueur du mot de passe
    caracteres = "0123456789"  # Caractères autorisés
    mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur))
    mdp_entry.delete(0, tk.END)
    mdp_entry.insert(tk.END, mot_de_passe)

def ajouter():
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    adresse = adresse_entry.get()
    mdp = mdp_entry.get()

    # Vérifier si tous les champs sont remplis
    if nom == "" or prenom == "" or adresse == "" or mdp == "":
        messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
        return

    # Vérifier si une image a été sélectionnée
    if not hasattr(canvas, "image"):
        messagebox.showwarning("Erreur", "Veuillez sélectionner une image.")
        return

    # Convertir l'image en données binaires encodées en base64
    image_pil = canvas.image
    image_byte_array = io.BytesIO()
    image_pil.save(image_byte_array, format='PNG')
    image_base64 = base64.b64encode(image_byte_array.getvalue()).decode('utf-8')

    # Connexion à la base de données
    conn = sqlite3.connect("test_Python.db")
    cursor = conn.cursor()

    # Supprimer la table utilisateurs si elle existe déjà
    cursor.execute("DROP TABLE IF EXISTS utilisateurs")

    # Création de la table avec la nouvelle structure
    cursor.execute('''CREATE TABLE utilisateurs
                  (nom TEXT, prenom TEXT, adresse TEXT, mdp TEXT, image_base64 TEXT)''')

    # Insertion des données dans la table
    cursor.execute("INSERT INTO utilisateurs VALUES (?, ?, ?, ?, ?)", (nom, prenom, adresse, mdp, image_base64))

    # Validation de la transaction
    conn.commit()

    # Fermeture de la connexion
    conn.close()

    # Réinitialisation des entrées
    reset()

    # Redirection vers l'interface utilisateur
    fenetre.destroy()
    subprocess.call(["python", "interface_utilisateur.py"])

def reset():
    nom_entry.delete(0, tk.END)
    prenom_entry.delete(0, tk.END)
    adresse_entry.delete(0, tk.END)
    mdp_entry.delete(0, tk.END)
    canvas.delete("all")

def quitter():
    fenetre.quit()

def parcourir_image():
    fichier = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg")])
    if fichier:
        # Charger l'image avec PIL
        image_pil = Image.open(fichier)

        # Redimensionner l'image si nécessaire
        image_pil = image_pil.resize((200, 150))

        # Convertir l'image PIL en objet compatible avec tkinter
        image = ImageTk.PhotoImage(image_pil)

        # Afficher l'image sélectionnée dans le canvas
        canvas.delete("all")
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.image = image  # Garder une référence à l'image

        # Convertir l'image en données binaires encodées en base64
        image_byte_array = io.BytesIO()
        image_pil.save(image_byte_array, format='PNG')
        image_base64 = base64.b64encode(image_byte_array.getvalue()).decode('utf-8')

        # Stocker l'image encodée en base64 dans le canvas
        canvas.image_base64 = image_base64

fenetre = tk.Tk()
fenetre.title("Inscription")
fenetre.geometry("600x400")
fenetre.resizable(False, False)
fenetre.config(background='yellow')

titre = tk.Label(fenetre, text='Inscription', fg="blue", bg='yellow', font=('Courier', 20, 'bold'))
titre.place(x=200, y=5)

label_nom = tk.Label(fenetre, text="Nom :", font=("Arial", 14), bg="yellow")
label_nom.place(x=30, y=70)
nom_entry = tk.Entry(fenetre)
nom_entry.place(x=90, y=73)

label_prenom = tk.Label(fenetre, text="Prenom :", font=("Arial", 14), bg="yellow")
label_prenom.place(x=20, y=100)
prenom_entry = tk.Entry(fenetre)
prenom_entry.place(x=104, y=103)

canvas = tk.Canvas(fenetre, width=155, height=120, bg="white")
canvas.place(x=420, y=75)

button_parcourir = tk.Button(fenetre, text="Insérer Image", command=parcourir_image)
button_parcourir.place(x=455, y=200)

label_adresse = tk.Label(fenetre, text="Adresse :", font=("Arial", 14), bg="yellow")
label_adresse.place(x=20, y=130)
adresse_entry = tk.Entry(fenetre)
adresse_entry.place(x=110, y=134)

label_mdp = tk.Label(fenetre, text="Mot de passe :", font=("Arial", 14), bg="yellow")
label_mdp.place(x=20, y=160)
mdp_entry = tk.Entry(fenetre, show="*")
mdp_entry.place(x=150, y=164)

button_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
button_quitter.place(x=190, y=280)

button_reset = tk.Button(fenetre, text="Reset", command=reset)
button_reset.place(x=300, y=280)

button_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter)
button_ajouter.place(x=420, y=280)

menu_bar = tk.Menu(fenetre)

# Menu "Fichier"
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Déjà Inscrit", command=connecter)
file_menu.add_command(label="Quitter", command=quitter)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

# Menu "Nouveau"
file_menu2 = tk.Menu(menu_bar, tearoff=0)
file_menu2.add_command(label="Inscription", )
file_menu2.add_command(label="Information", command=ouvrir_fenetre)
menu_bar.add_cascade(label="Nouveau", menu=file_menu2)

fenetre.config(menu=menu_bar)
fenetre.mainloop()
