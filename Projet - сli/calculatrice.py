


# Calculatrice
# Operations:
"""
1) Addition
2) Soustraction
3) Multiplication
4) Division
5) Au carré
6) Racine Carré
"""

# L'utilisateur choisira une option entre 1 et 6.

msg_de_presentation = """
Bienvenue dans le monde de la calculatrice !!!
"""

msg_des_choices = """
Choisis une option entre 1 et 6:
	1) Addition
	2) Soustraction
	3) Multiplication
	4) Division
Ton choix:
"""


print(msg_de_presentation)

def ask_choice(minimum, maximum):
    continuer = True
    while continuer:
        choice = input(msg_des_choices)

        if choice.isnumeric():

            choice_int = int(choice)

            if minimum <= choice_int <= maximum:
                break

            else:
                print("Choisis un nombre entre {} et {}!!!".format(minimum, maximum))

        else:
            print("c'est un mauvais nombre.\nRentres un nombre valide")

    return choice_int

def ask_number(msg):
    while True:
        nombre = input(msg	)
        if nombre.isnumeric():
            nombre = int(nombre)
            return nombre
        else: print("ce nest pas un nombre")

def additiion(a, b):
    return a+b

def soustraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

fonctions = {
    1:additiion,
    2:soustraction,
    3:multiplication,
    4:division,
                }
choix = ask_choice(1, 4)
nombre1 = ask_number("Quel est le premier nombre: ")
nombre2 = ask_number("Quel est le deuxieme nombre: ")
fonction_calcul = fonctions[choix]
resultat = fonction_calcul(nombre1, nombre2)
print("Le resultat est: ",resultat)






