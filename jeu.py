
import random
import time 
# Différentes librairies natives utilisées
# On demande à l'utilisateur de choisir le niveau
niveau = input("     Choisis ton niveau de difficulté (facile = 1, difficile = 2) : ")
# Le prix est généré en fonction du niveau choisi
grand_prix = 50             # Valeur par défaut du grand prix 
if niveau == "1":
    print("     Tu as choisi le niveau facile")

elif niveau == "2":
    grand_prix = 500
    print("     Tu as choisi le niveau difficile ")
    
else:
    print("    😡  Niveau de difficulté pas valide, le jeu se lance en mode facile par défaut ")

prix = random.randint(1,grand_prix)
devine = (f"     Devine le prix entre 1 et {grand_prix} : ")
debut_chrono = time.time()
compteur: int = 0

print( devine) 
# On débute une boucle tant que "prix" est différent de "devine". Au début elle l'est car ce n'est même pas un nombre entier 
while devine != prix:
    compteur += 1
    # On demande à l'utilisateur de deviner
    devine = input("     \n     ").strip()
    # On vérifie que "devine" est un nombre entier
    if devine.isdigit() == False:
        print(f"     😡 !! \"{devine}\" n'est pas un nombre, essaie encore !!\n")
        # On remonte au haut de la boucle
        continue
    
    # On convertit "devine" en entier pour pouvoir le comparer
    devine = int(devine)
    if devine < prix:
        print("     C'est trop petit !!")
        print("     Réessaie encore")
    elif devine > prix:
        print("     C'est trop grand !!")
        print("     Réessaie encore")

fin_chrono = time.time()
chrono = int(fin_chrono-debut_chrono)
# On convertit les secondes en minutes et secondes
minutes, secondes = divmod(chrono, 60)

if minutes == 0:
     print(f"     Bravo tu as trouvé le prix en {compteur} tentatives en {secondes}s !")
else:
    print(f"     Bravo tu as trouvé le prix en {compteur} tentatives et en {minutes}m {secondes}s !")