import random
import time 
#differentes librairies utilisées
#on demande a l'utilisateur de choisir le niveau
niveau = input("     Choisis ton niveau de difficulté (facile = 1, difficile = 2) : ")
# le prix est generer en fonction du iveau choisi
if niveau == "1":
    prix = random.randint(1, 50)
    grand_prix = 50
elif niveau == "2":
    prix = random.randint(1, 500)
    grand_prix = 100
else:
    print("     Niveau de difficulté pas valide, le jeu se lance en mode facile par défaut")
    prix = random.randint(1,5) 
    grand_prix = 50

debut_chrono = time.time()
#on ajoute le grand prix dans le texte
devine = (f"     Devine le prix entre 1 et {grand_prix} : ")
compteur: int = 0
print( devine) 
#on debute une boucle tant que "prix" est different de "devine" zu debut elle l'est car ce n'est meme pas un nombre entier 
while devine != prix:
    compteur += 1
    # on demande à l'utilisateur de deviner
    devine = input("     \n     ")
    #on verifie que "devine" est un nombre entier
    if devine.isdigit() == False:
        print("     !!Ce n'est pas un nombre, essaie encore !!😡\n")
        #on remonte au haut de la boucle
        continue
    
    #on cnvertie " devine" en entier pour povoir le comparer
    devine = int(devine)
    if devine < prix:
        print("     C'est trop petit !!")
        print("     Réessaie encore")
    elif devine > prix:
        print("     C'est trop grand !!")
        print("     Réessaie encore")

fin_chrono = time.time()
chrono = int(fin_chrono-debut_chrono)
#on convertie les secondes en minutes et secondes
minutes, secondes = divmod(chrono, 60)

if minutes == 0:
     print(f"     Bravo tu as trouvé le prix en {compteur} tentatives en {secondes}s !")
else:
    print(f"     Bravo tu as trouvé le prix en {compteur} tentatives et en {minutes}m {secondes}s !")