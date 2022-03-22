# Créé par tmicetic, le 22/03/2022 en Python 3.7
import random

labyrinthe = [
  [[2, False, True, True, False],[2, False, True, False, True],[2, False, True, False, True],[1, False, False, False, True]],
  [[2, True, False, True, False],[2, False, True, False, False],[2, False, True, True, True],[0, False, False, True, True]],
  [[2, True, True, False, False],[2, False, False, True, True],[2, True, False, True, False],[2, True, False, True, False]],
  [[2, False, False, True, False],[2, True, True, False, False],[2, True, False, False, True],[2, False, True, False, False]],
]

for i in range(len(labyrinthe)):
    sousliste = labyrinthe[i]
    print(sousliste)

def definir_entree_sorite():
    """ Fonction qui définit l'entrée et la sortie du labyrinthe """
    premier_cote = random.randint(1, 2)
    if premier_cote == 1:
        deuxieme_cote = 3
    elif premier_cote == 2:
        deuxieme_cote = 4
    for i in range(len(labyrinthe)):
        for elements in labyrinthe[i]:
            labyrinthe[i][0] = 2
    carre_entree = random.randint(1, 15)
    carre_sortie = random.randint(1, 15)
    carre_actuel = labyrinthe[carre_entree]
    carre_actuel[0] = 1
    carre_actuel[1] = True
