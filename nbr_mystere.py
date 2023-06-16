from random import randint

nbr_valid = randint(1, 100)

print("Voici le jeu du nombre mystere :)")
i = 5
while True:

    print("Choisi un nombre entre 1 et 100 :")
    nbr_choisi = input("")

    if int(nbr_choisi) > nbr_valid and i != 1 and int(nbr_choisi) <= 100:
        print("C'est plus petit")
        i -= 1
        print(f"Il te reste {i} essais")
    elif int(nbr_choisi) < nbr_valid and i != 1 and int(nbr_choisi) <= 100:
        print("C'est plus grand")
        i -= 1
        print(f"Il te reste {i} essais")
    elif int(nbr_choisi) == nbr_valid:
        print("Tu as gagné !!")
        break
    elif i == 1:
        print("Tu as perdu !!")
        break
    elif int(nbr_choisi) > 100:
        print("Le nombre doit être entre 1 et 100")
