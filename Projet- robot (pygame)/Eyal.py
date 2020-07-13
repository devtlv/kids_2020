import pgzrun

bonhomme = Actor("character_robot_attackkick")

WIDTH = 720

HEIGHT = 720


def draw():
    screen.fill((16, 83, 147))
    bonhomme.draw()


def update():
    if bonhomme.y < 0:
        bonhomme.y = HEIGHT




    if keyboard.up:
            print("tu appuye sur espace")
            bonhomme.y -= 10
    if keyboard.down:
        bonhomme.y += 10
    if keyboard.right:
        bonhomme.x += 10
    if keyboard.left:
        bonhomme.x -= 10


def on_mouse_down(pos):
    if bonhomme.collidepoint(pos):
        print("tu mas touchee")
        bonhomme.image = "sirius"


    else:
        print("OUPS")



pgzrun.go()