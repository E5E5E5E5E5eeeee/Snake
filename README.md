# 🐍 Jeu Snake - Processing (Python)

Jeu de Snake classique développé dans le cadre de ma dèrnière année de lycée. 

## 🎮 Aperçu
![Capture d'écran du jeu](screenshots/gameplay.png) ## 🛠️ Installation et Utilisation

Ce jeu a été conçu avec l'environnement **Processing**. Pour y jouer :

1. **Téléchargez Processing** : Rendez-vous sur [processing.org](https://processing.org/download/).
2. **Ajoutez le mode Python** :
   - Ouvrez Processing.
   - Cliquez sur le menu en haut à droite (par défaut "Java").
   - Sélectionnez "Add Mode..." et installez **Python Mode**.
3. **Lancez le jeu** :
   - Téléchargez ce dépôt GitHub.
   - Ouvrez le fichier `Snake.pyde` avec Processing.
   - Appuyez sur le bouton **Exécuter** (la flèche "Play").

## ⌨️ Commandes
* **Flèches directionnelles** : Déplacer le serpent.
* **Objectif** : Manger les pastilles roses pour gagner des points sans toucher les bords ou votre propre corps.

## 📁 Structure du code
* `Snake.pyde` : Gère la boucle principale (`setup` et `draw`) et les entrées clavier.
* `fonction.py` : Contient la logique métier (déplacement, collisions, affichage).
