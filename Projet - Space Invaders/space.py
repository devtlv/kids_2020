import pygame
import random
import math
from pygame import mixer

# Initialiser pygame
pygame.init()

# Creer une surface
size = (800, 600)
screen = pygame.display.set_mode(size)

background = pygame.image.load('images/background1.png')


class Vaisseau:
    def __init__(self):
        self.actor = pygame.image.load('images/spaceship.png')
        self.actor = pygame.transform.scale(self.actor, (100, 100))

        self.x = 400
        self.y = 400

    def draw(self):
        screen.blit(self.actor, (self.x, self.y))

    def move(self, dx):
        self.x += dx

        # Les limites
        # Cote gauche
        if self.x <= 0:
            self.x = 0
        # Cote droit
        elif self.x >= 700:
            self.x = 700


vaisseau = Vaisseau()

# Load images
# vaisseau = pygame.image.load('images/spaceship.png')
# vaisseau = pygame.transform.scale(vaisseau, (100, 100))
# vaisseau_x = 400
# vaisseau_y = 400

# Mouvement du vaisseau
# vaisseau_dx = 0

# Sons du background
# mixer.music.load('sounds/background.wav')
# mixer.music.play(-1)

fin_jeu = False


class Alien:
    def __init__(self, x):
        self.actor = pygame.image.load('images/alien.png')
        self.actor = pygame.transform.scale(self.actor, (70, 70))

        self.alive = True

        self.x = x
        self.y = random.randint(50, 150)

        self.dx = 10
        self.dy = 40

    def draw(self, screen):
        if self.alive:
            screen.blit(self.actor, (self.x, self.y))

    def move(self):

        if self.x <= 0:
            self.dx = 10
            self.y += self.dy
        # Cote droit
        elif self.x >= 730:
            self.x = 730
            self.dx = -10
            self.y += self.dy

        self.x += self.dx
 
        


# Etape 2 : Creer une liste d'aliens
n_aliens = 5
x = 10
ecart = 100
aliens = []

for i in range(n_aliens):
    alien = Alien(x)
    aliens.append(alien)
    x += ecart


class Balle:
    def __init__(self):
        self.actor = pygame.image.load('images/bullet.png')
        self.actor = pygame.transform.scale(self.actor, (70, 70))

        self.x = 0
        self.y = 400

        self.dx = 0
        self.dy = 20

        # Pret = tu peux tirer
        # Feu = Tu peux pas encore tirer parce qu'il y'a deja une balle
        self.etat = 'pret'

        # Hitbox
        self.hitbox = 40

        # Son
        self.son = mixer.Sound('sounds/laser.wav')

    def draw(self):
        screen.blit(self.actor, (self.x, self.y))

    # Pas encore termine
    # Lorsqu'on tire une balle
    def tirer_balle(self, x, y):
        self.etat = 'feu'
        self.x = x
        self.draw()

        if y <= 0:
            self.etat = 'pret'
            self.y = 400

    def play_sound(self):
        self.son.play()


balle = Balle()

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_X = 10
text_Y = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    # font.render(Texte, MONTRER?, color)
    over_text = over_font.render("GAME OVER !", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def montrer_score(x, y):
    # font.render(Texte, MONTRER?, color)
    score_text = font.render("Score: {}".format(score), True, (255, 255, 255))
    screen.blit(score_text, (x, y))


def distance(point1, point2):
    # chaque point --> (x,y)
    x1 = point1[0]
    y1 = point1[1]

    x2 = point2[0]
    y2 = point2[1]

    # math.sqrt (square root) -> racine carree
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance


dx = 0
# Boucle de jeu
continuer = True
while continuer:
    screen.fill((0, 0, 0))
    # Fond d'ecran
    screen.blit(background, (0, 0))

    # Recuperer les evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Arrete la boucle de jeu
            continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -15
            if event.key == pygame.K_RIGHT:
                dx = 15
            if event.key == pygame.K_SPACE:
                # Pour que la balle suive sa trajectoire..
                if balle.etat == 'pret':
                    balle.play_sound()
                    balle.tirer_balle(vaisseau.x + 15, balle.y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                dx = 0

    vaisseau.move(dx)

    # Continuer la balle
    if balle.etat == 'feu':
        balle.tirer_balle(balle.x, balle.y)
        balle.y -= balle.dy

    for alien in aliens:
        if not alien.alive:
            continue

        # Game Over
        if alien.y > 350:
            for ali in aliens:
                ali.alive = False
                ali.draw(screen)
            fin_jeu = True
            break

        alien.move()

        # Regarder si la balle a touche le rabbin
        alien_balle_distance = distance([balle.x, balle.y], [alien.x, alien.y])

        # Si la balle touche l'alien, l'alien disparait
        if alien_balle_distance <= balle.hitbox:
            # Ajout du score
            score += 1

            explosion_son = mixer.Sound('sounds/explosion.wav')
            explosion_son.play()

            # Faire disparaitre l'alien
            alien.alive = False

            # Faire disparaitre la balle
            balle.etat = 'pret'
            balle.y = 400

        alien.draw(screen)

    vaisseau.draw()
    # On appelle la fonction pour montrer le texte
    montrer_score(text_X, text_Y)
    # Si le jeu est fini alors montrer game over
    if fin_jeu:
        game_over_text()

    # Rafraichir l'ecran
    pygame.display.update()
