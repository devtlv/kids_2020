"""
Aujourdhui

1. Courses -- Fait
2. Repas -- A faire
3. Lire -- Fait

TODO: Mettre fait ou pas fait
"""
import sys

mgs_presentation = """
Bienvenue dans la To-Do-List:
Quelle option veux-tu choisir ?

	1) Voir mes taches.
	2) Rajouter une tache.
	3) Supprimer une tache.
	4) Sortir.

"""


taches = []


# Creer une fonction montrer_tache() qui presentera un print a l'utilisateur avec
# toutes les taches qui sont dans la liste tache
# Quand l'option choisit est 1.


def montrer_tache():
    print("Voici les taches:")
    for tache in taches:
	    print(tache)


def ajouter_tache():
	yo = input("que veux tu ajouter dans ta liste: ")
	taches.append(yo)
	montrer_tache()


def supprimer_tache():

	for index, tache in enumerate(taches):
		print("{}: {}".format(index, tache))


	tut = ask_choice(0, len(taches),"choisis un nombre en fonction de la tache que tu souhsite supprimer: " )
	taches.pop(tut)
	montrer_tache()


def ask_choice(minimum, maximum, msg):
	continuer = True
	while continuer:
		choice = input(msg)

		if choice.isnumeric():

			choice_int = int(choice)

			if minimum <= choice_int <= maximum:
				break

			else:
				print("Choisis un nombre entre {} et {}!!!".format(minimum, maximum))

		else:
			print("c'est un mauvais nombre.\nRentres un nombre valide")

	return choice_int


def sortir():
	print("Merci, au revoir !")
	sys.exit(0)

fonctions = {
	# key: value
	1: montrer_tache,
	2: ajouter_tache,
	3: supprimer_tache,
	4:sortir
}

# variable[key]




def to_do_list():
	choix = ask_choice(1, 4, mgs_presentation)

	fonction_calcul = fonctions[choix]

	fonction_calcul()

while True:
	to_do_list()
