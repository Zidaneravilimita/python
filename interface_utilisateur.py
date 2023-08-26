import tkinter as tk

dev = tk.Tk()
dev.title("Utilisateur")
dev.geometry("700x400")
dev.config(background="#FFFFFF")  # Couleur de fond de la fenêtre principale

# Ajoutez les éléments et la logique de l'interface utilisateur ici
titre = tk.Label(dev, text="Bienvenue dans l'interface de l'utilisateur", font=("Arial", 14),
                 bg="#FFA500", fg="#FFFFFF")
titre.pack(pady=10)

dev.mainloop()
