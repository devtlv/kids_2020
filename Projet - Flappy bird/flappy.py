import pgzrun
import random

import time


HEIGHT = 708
WIDTH = 400
GRAVITY = 3
FLAP = 5
ECART= 700
mort = False
SCORE = 0


oiseau = Actor("oiseau", (75, 200))

def reset_tuyaux():
    num_haut = random.randint(200, HEIGHT - 200)
    tuyau_haut.pos = (WIDTH, num_haut - ECART // 2 )
    tuyau_bas.pos = (WIDTH, num_haut + ECART // 2 )
    print("tuyeauhaut: {}".format(tuyau_haut.pos))

    #tuyau_bas.pos = (WIDTH, num_haut + ECART)
    print(num_haut)


tuyau_haut = Actor("tuyeauhaut")
tuyau_bas = Actor("tuyeau")
reset_tuyaux()

def draw():
    screen.blit("fond", (0, 0))
    tuyau_haut.draw()
    tuyau_bas.draw()
    oiseau.draw()

def update_tuyaux():
    tuyau_bas.left -= 3
    tuyau_haut.left -= 3
    #z  z   print(tuyau_bas.left)
    if tuyau_bas.right < -20:
        reset_tuyaux()

def update_oiseau():
    oiseau.y += GRAVITY

def update():
    global mort
    if mort == True:
        oiseau.y += 25
    else:
        update_tuyaux()
        update_oiseau()

        if oiseau.y > HEIGHT:
            print("tu es tombee")
            mort = True

        if oiseau.x > tuyau_bas.x:
            print(SCORE == SCORE + 1)



        if oiseau.y < 0:
            print(" tu es aller trop haut")
            mort = True
            dead = Actor("saut")
        if oiseau.colliderect(tuyau_haut) or oiseau.colliderect(tuyau_bas):
            print ("AIE")
            oiseau.image = "saut"
            mort = True

def on_key_down():
    if keyboard.up:
        oiseau.y -= 75
    if keyboard.down:
        oiseau.y += 40


pgzrun.go()