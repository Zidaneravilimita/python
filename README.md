# Application d'Inscription avec Interface Utilisateur

**Description**
Ceci est une application Python d'inscription avec une interface utilisateur graphique (GUI) développée en utilisant la bibliothèque tkinter. L'application permet aux utilisateurs de s'inscrire en fournissant leur nom, prénom, adresse, mot de passe, et en téléchargeant une image de profil.

¤L'application stocke les données des utilisateurs dans une base de données SQLite, y compris l'image de profil encodée en base64. Elle offre également des fonctionnalités pour réinitialiser les champs, parcourir et sélectionner une image, quitter l'application, et rediriger vers une interface utilisateur principale.

**Fonctionnalités principales**
1. **Inscription d'utilisateur** : Les utilisateurs peuvent saisir leur nom, prénom, adresse et générer un mot de passe aléatoire. Ils peuvent également télécharger une image de profil.

2. **Sélection d'image** : Les utilisateurs peuvent parcourir leur système de fichiers pour sélectionner une image de profil, qui est ensuite affichée dans un canvas.

3. **Stockage en base de données** : Les données de l'utilisateur, y compris l'image encodée en base64, sont stockées dans une base de données SQLite.

4. **Réinitialisation des champs** : Les utilisateurs peuvent réinitialiser tous les champs du formulaire en appuyant sur le bouton "Reset".

5. **Menu de navigation** : Le menu supérieur offre des options pour quitter l'application ou accéder à une autre interface utilisateur.

**Utilisation**
1. Remplissez les champs "Nom", "Prénom", "Adresse", et générez un mot de passe si nécessaire.
2. Cliquez sur le bouton "Insérer Image" pour sélectionner une image de profil.
3. Vous pouvez réinitialiser les champs en cliquant sur "Reset".
4. Cliquez sur "Ajouter" pour enregistrer les informations dans la base de données.
5. Utilisez le menu supérieur pour naviguer vers d'autres fonctionnalités de l'application.

**Contexte de Code Python - Système d'Authentification Utilisateur avec Interface Graphique**

Ce code Python implémente un système d'authentification utilisateur avec une interface graphique développée en utilisant la bibliothèque Tkinter. L'application permet aux utilisateurs de se connecter en fournissant leur nom d'utilisateur et leur mot de passe. Voici une description détaillée des fonctionnalités de l'application :

1. **Interface Utilisateur** :
   - L'application crée une fenêtre principale avec une dimension de 900x500 pixels et un fond blanc.
   - Elle ajoute une image de fond à la fenêtre principale pour une meilleure expérience utilisateur.

2. **Champ de Saisie** :
   - Il y a deux champs de saisie : "Nom" et "Mot de passe".
   - L'utilisateur est invité à entrer son nom et son mot de passe.

3. **Validation du Formulaire** :
   - Lorsque l'utilisateur clique sur le bouton "Valider", le code vérifie les informations fournies dans les champs de saisie.
   - Il établit une connexion à une base de données SQLite nommée "test_Python.db".
   - Ensuite, il effectue une requête SQL pour vérifier si un utilisateur avec le nom d'utilisateur et le mot de passe fournis existe dans la base de données.
   - Si un utilisateur correspondant est trouvé, une boîte de dialogue affiche "Validation réussie" et l'utilisateur est redirigé vers une interface utilisateur.
   - Sinon, une boîte de dialogue affiche "Erreur de validation" avec le message "Nom ou mot de passe incorrect".

4. **Réinitialisation des Champs** :
   - L'utilisateur peut cliquer sur le bouton "Reset" pour effacer les champs de saisie du nom et du mot de passe.

5. **Création d'un Compte** :
   - En bas de la fenêtre, il y a un lien "Créer un compte ?" qui encourage l'utilisateur à s'inscrire.
   - Lorsque l'utilisateur clique sur le bouton "Sign Up", il est redirigé vers un autre module Python nommé "zidane.py", supposément utilisé pour l'inscription.

6. **Autres Éléments d'Interface Utilisateur** :
   - Un titre "Sign In" est affiché en haut de la fenêtre.
   - Les boutons "Valider" et "Reset" sont disponibles pour soumettre le formulaire ou effacer les champs respectivement.
   - Les éléments visuels sont configurés avec différentes couleurs pour l'arrière-plan, la police, etc., pour une meilleure apparence.

7. **Boucle Principale Tkinter** :
   - La boucle principale Tkinter `dev.mainloop()` est utilisée pour exécuter l'interface graphique, ce qui signifie que l'application attend les interactions de l'utilisateur.


**Dépendances**
- Python 3.x
- tkinter
- SQLite3
- PIL (Pillow) pour la gestion des images

**Auteur**
zidaneravilimita@gmail.com

**Remarque :** Cette application est actuellement en développement. Si vous avez des idées pour améliorer mon projet, n'hésitez pas à le modifier ou à me contacter. Merci d'avance pour votre aide !
