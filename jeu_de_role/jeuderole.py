import random
import emoji

# Initialisation des variables

points_de_vie_joueur = 50
points_de_vie_ennemi = 50
Nbre_de_potions = 3
choix_joueur = 0
points_de_vie_recuperes = 0



while int(points_de_vie_joueur) > 0 and int(points_de_vie_ennemi) > 0:
    if int(points_de_vie_joueur) != 50 or int(points_de_vie_ennemi) !=50:
        print(f"il vous reste {points_de_vie_joueur} points de vie")
        print(f"Il reste {points_de_vie_ennemi} points de vie à l'ennemi")
    while int(choix_joueur) != 1 or int(choix_joueur) != 2:
        choix_joueur =input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
    
        if int(choix_joueur) == 1:
            print(emoji.emojize("Vous lancez une attaque :thumbs_up:"))
            degats_a_l_ennemi = random.randint(5, 10)
            degats_au_joueur = random.randint(5, 15)
            print(f"Vous avez infligé {degats_a_l_ennemi} points de dégats à l'ennemi")
            print(f"L'ennemi vous a infligé {degats_au_joueur} points de dégâts")
            points_de_vie_joueur -= degats_au_joueur
            points_de_vie_ennemi -= degats_a_l_ennemi
            choix_joueur = 0
            break
        elif int(choix_joueur) == 2:
            if int(Nbre_de_potions) > 0:
                Nbre_de_potions -= 1
                points_de_vie_recuperes = random.randint(15, 50)
                print(f"Vous récuperez {points_de_vie_recuperes} points de vie ({Nbre_de_potions} potion restantes)")
                points_de_vie_joueur += points_de_vie_recuperes
                degats_au_joueur = random.randint(5, 15)
                points_de_vie_joueur -= degats_au_joueur
                choix_joueur = 0
                break
            else:
                print("Vous n'avez plus de potion")
                break
        
if int(points_de_vie_joueur) > 0:
    print("Vous avez gagné !")
    
else:
    print("Vous avez perdu !")
    
    