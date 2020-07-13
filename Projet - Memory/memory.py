# Importer les modules dont on a besoin
import pgzrun
import random

# Creer les acteurs
bonne_carte = Actor('checkmark')            # Image quand la carte est bonne
dos_carte   = Actor('card_back', (50,50))     # Image du dos de la carte

# Creer la configuration
nb_colonnes = 4                             # Nombre de colonnes
nb_lignes   = 3                               # Nombre de lignes
taille_img  = 200                            # Taille de chaque carte

# Creer une liste d'images
liste_images = ['im1', 'im2', 'im3', 'im4', 'im5', 'im6', 'im1', 'im2', 'im3', 'im4', 'im5', 'im6']

# Creer des listes de status
cartes_cliquees = []
cartes_trouvees = []

# Melanger la liste grace a random.shuffle
random.shuffle(liste_images)

# Creer un tableau
tableau = []
for ligne in range(nb_lignes):
    nv_ligne = []

    # Mettre des images
    for colonne in range(nb_colonnes):

        # Prendre une image dans la liste
        nom_image = liste_images.pop()      # Pop prend la derniere image de la liste, ca l'efface et
                                        # ca la met dans image

        # Creer un acteur
        # On cree un acteur avec le nom de l'image
        actor         = Actor(nom_image, (taille_img*colonne, taille_img*ligne))
        actor.topleft = (taille_img*colonne, taille_img*ligne)
        actor.valeur  = nom_image

        # Mettre cet acteur dans nv_ligne
        nv_ligne.append(actor)

    # Mettre nv_ligne dans tableau
    tableau.append(nv_ligne)


def draw():

    # Dessiner toutes les cartes de dos
    for ligne in range(nb_lignes):
        for colonne in range(nb_colonnes):

            # Verifier si la carte a ete cliquee
            ix = (ligne, colonne)

            if ix in cartes_cliquees:
                # Tableau ressemble a ca:
                # [
                #       [Image1, Image2, Image3]
                #       [Image5, Image6, Image7]
                # ]
                image_carte = tableau[ligne][colonne]
                image_carte.draw()
            elif ix in cartes_trouvees:
                bonne_carte.topleft = (taille_img*colonne, taille_img*ligne)
                bonne_carte.draw()

            else:
                dos_carte.topleft = (taille_img*colonne, taille_img*ligne)
                dos_carte.draw()


def on_mouse_down(pos, button):
    # Comment faire ?
    # index = (position_x * taille_img, position_y * taille_img)
    # position = (index_x // taille_img, index_y // taille_img)
    if len(cartes_cliquees) == 2:
        return False

    if button != mouse.LEFT:
        return False

    # Recuperer l'index de la carte
    carte_y = pos[0]
    carte_x = pos[1]

    carte_ix = (carte_x // taille_img, carte_y // taille_img)

    if carte_ix not in cartes_cliquees:
        cartes_cliquees.append(carte_ix)
        # Premiere carte cliquee -> on fait rien
        # Deuxieme carte cliquee
        if len(cartes_cliquees) == 2:
            # Recuperer les deux cartes cliquees
            carte1_ix = cartes_cliquees[0] # (x, y)
            carte2_ix = cartes_cliquees[1] # (x, y)

            carte1 = tableau[carte1_ix[0]][carte1_ix[1]]
            carte2 = tableau[carte2_ix[0]][carte2_ix[1]]

            # Checker si c'est les memes
            if carte1.valeur == carte2.valeur:
                # Si oui, j'ajoute les deux cartes a cartes_trouvees
                cartes_trouvees.append(carte1_ix)
                cartes_trouvees.append(carte2_ix)

            # Passer un tour -->
            clock.schedule_unique(next_turn, 2)

def next_turn():
    cartes_cliquees.clear()









# Ligne obligatoire:
pgzrun.go()