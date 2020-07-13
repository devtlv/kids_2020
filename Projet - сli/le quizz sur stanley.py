print("bienvenue sur le quizz pour savoir si vous savez tous sur stanley")
shit = input("es tu pret ?")
if shit == "oui":
    print("on est partie !")
    print("premiere question")
    kraken= int(input("quelle age a stanley?"))
    if kraken == 14:
        print("bonne reponse !!")
        print("deuxieme question")
        chocolat = input("comment sappelle les chiens de stanley")
        if chocolat == "blacky fidji" or chocolat == "fidji blacky":
            print("Bonne reponse !!")
            print("troiseme question")
            cat = input("comment es que les amis de belgique appelle satnley?")
            if cat =="stoon" or cat =="Stoon":
                print("bravo!!")
                print("quatrieme question")
                yo = input("quelle est le mois de la naissance de stanley ")
                if yo =="septembre":
                    print("bonne reponse")
                    print("question suivante")
                    mousse=input("quelle est le restaurant ou stanley mange tout le temps")
                    if mousse == "japanika":
                        print("tu es tres fort")
                        print("6 eme question")
                        vie = input("quelle est le theme de la chambre de stanley")
                        if vie == "londre":
                            print("tu me connais bien toi")
                            print("ca pars sur le 7 eme question")
                            niche = input("comment sappelle le grand pere de stanley (du cote de son pere)")
                            if niche == "david":
                                print("quelle talent !!")
                                print("question suivante cette question est dur")
                                toi = input("quelle est la marque de la television de stanley(celle dans sa chambre)")
                                if toi == "philips":
                                    print("tu es vraiment incroyable")
                                    print("je me souvien plus du nombre de la question mais c pas grave on est partie c encore une fois une question dur mais je crois en toi")
                                    mine = input("quelle est la marque de la montre que son grand pere lui a offert")
                                    if mine == "fossil":
                                        print("waouwwwww")



                else:
                    print("game over")
            else:
                print("nul germain NUL!!!!!")
        else:
            print("je te pensais plus fort que ca")



    else:
        print("tu me decois de ouf")


