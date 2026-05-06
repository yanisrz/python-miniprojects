import random
import time 
prix = random.randint(1, 50)
debut_chrono = time.time()
devine="     Devines le prix entre 1 et 50: "
compteur: int = 0
print( devine )
while devine != prix:
    compteur += 1
    devine = input("     \n     ")
    if devine.isdigit() == False:
        print("     !!Ce n'est pas un nombre, essaye encore!!😡\n")
        continue
    devine = int(devine)
    if devine < prix:
        print("     C'est trop petit !!")
        print("     reessaie encore")
    elif devine > prix:
        print("     C'est trop grand !!")
        print("     reessaie encore")

fin_chrono = time.time()
chrono = int(fin_chrono-debut_chrono)
print(f"     Bravo tu as trouve le prix en {compteur} tentatives et en {chrono}s!")
    
   


