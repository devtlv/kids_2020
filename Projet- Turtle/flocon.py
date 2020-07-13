import turtle

t = turtle.Pen()

def branche(size):
    t.forward(size / 3)
    for n in range(2):
        t.forward(size / 3)
        t.backward(size / 3)
        t.right(45)
        t.forward(size / 3)
        t.backward(size / 3)
        t.left(90)
        t.forward(size / 3)
        t.backward(size / 3)
        t.right(45)
        t.forward(size / 3)
    t.backward(size)


def flocon(nb_de_branches, size):
    angle = 360 / nb_de_branches
    for n in range(nb_de_branches):
        branche(size)
        t.right(angle)

flocon(10, 150)


branche(50)
