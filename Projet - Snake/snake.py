


import pygame
import time
import random

pygame.init()
# La taille de la fenetre
size = (800, 600)
screen = pygame.display.set_mode(size)
points = 0
#
# class Grid:
#
#     def __init__(self, rows, cols, scale):
#         # Taille de la grille
#         self.rows = rows  # Lignes
#         self.cols = cols  # Colonnes
#
#         self.scale = scale  # Echelle - Taille du cube
#
#         # Init grid
#         self.array = []
#
#         for row in range(self.rows * self.scale):
#             row_array = []
#
#             for col in range(self.cols * self.scale):
#                 row_array.append((125, 125, 125))
#
#             self.array.append(row_array)
#
#     def index2coords(self, coords):
#
#         x = coords[0]
#         y = coords[1]
#
#         ix = [x * self.scale, y * self.scale]  #
#
#         return ix


class Cube:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        # self.index = (x, y)
        self.color = color

    def draw_cube(self):
        # Rect(X, Y, largeur, hauteur)
        cube = pygame.Rect(self.x, self.y, 10, 10)
        cube.x = self.x
        # surface, couleur, coordonees
        pygame.draw.rect(screen, self.color, cube)


class Pomme(Cube):
    def teleportation(self, x, y):
        self.x = x
        self.y = y

    def check_location_apple(self, apple_x, apple_y):
        for serp_cube in serpent.cubes:
            if serp_cube.x == apple_x and serp_cube.y == apple_y:
                # La pomme est sur le serpent
                return True
        return False

    def random_apple(self):
        rand_x = random.randint(0, 79) * 10
        rand_y = random.randint(0, 59) * 10

        while self.check_location_apple(rand_x, rand_y):
            rand_x = random.randint(0, 79) * 10
            rand_y = random.randint(0, 59) * 10

        self.x = rand_x
        self.y = rand_y


class Snake:
    def __init__(self):
        self.couleur = (0, 255, 42)
        self.cubes = [Cube(400, 300, self.couleur), Cube(390, 300, self.couleur)]
        self.heading = None
    def get_head(self):
        return self.cubes[0]


    def cogne_lui_meme(self):
        head = self.get_head()
        for cube in self.cubes[1:]:
            if head.x == cube.x and head.y == cube.y:
                print("ohh merde")

    def deplacement(self, direction):
        global size

        # On enleve le dernier element de la liste
        self.cubes.pop()
        # On copie le premier cube
        head = self.cubes[0]

        # Droite: x + 10
        if direction == 'right':
            nouveau_cube = Cube(head.x + 10, head.y, self.couleur)

        # Gauche: x - 10
        elif direction == 'left':
            nouveau_cube = Cube(head.x - 10, head.y, self.couleur)

        # Haut: y - 10
        elif direction == 'up':
            nouveau_cube = Cube(head.x, head.y - 10, self.couleur)

        # Bas: y + 10
        elif direction == 'down':
            nouveau_cube = Cube(head.x, head.y + 10, self.couleur)

        # Regarder si le snake a pas depasse les bords
        if nouveau_cube.x <= 0:
            nouveau_cube.x = size[0] - 10  # X Max

        elif nouveau_cube.x >= size[0]:
            nouveau_cube.x = 0

        elif nouveau_cube.y <= 0:
            nouveau_cube.y = size[1] - 10  # X Max

        elif nouveau_cube.y >= size[1]:
            nouveau_cube.y = 0

        self.cubes.insert(0, nouveau_cube)

    def grandir(self):
        dernier_cube = self.cubes[-1]

        nouveau_cube = Cube(dernier_cube.x,dernier_cube.y , self.couleur)
        self.cubes.append(nouveau_cube)


# grid = Grid(80, 60, 10)

def snake_mange_pomme(snake, pomme):

    if (snake.get_head().x == pomme.x) and pomme.y == (snake.get_head().y):
        return True
    else:
        return False


serpent = Snake()

pomme = Pomme(250, 480, (255, 0, 0))


continuer = True

direction = 'right'

while continuer:
    # Reinitialier l'ecran
    screen.fill((0, 0, 0))

    # Evenements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction != 'right':
                    direction = 'left'
            if event.key == pygame.K_RIGHT:
                if direction != 'left':
                    direction = 'right'
            if event.key == pygame.K_UP:
                if direction != 'down':
                    direction = 'up'
            if event.key == pygame.K_DOWN:
                if direction != 'up':
                    direction = 'down'

    for serpent_cube in serpent.cubes:
        serpent_cube.draw_cube()

    serpent.deplacement(direction)
    pomme_mangee = snake_mange_pomme(serpent, pomme)
    if pomme_mangee == True:
        pomme.random_apple()
        points += 1
        print("miam miam")
        serpent.grandir()

    pomme.draw_cube()

    time.sleep(0.05)

    serpent.cogne_lui_meme()
    pygame.display.flip()


