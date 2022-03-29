# Créé par tmicetic, le 22/03/2022 en Python 3.7
import random

lab = [
  [[2, False, True, True, False],[2, False, True, False, True],[2, False, True, False, True],[1, False, False, False, True]],
  [[2, True, False, True, False],[2, False, True, False, False],[2, False, True, True, True],[0, False, False, True, True]],
  [[2, True, True, False, False],[2, False, False, True, True],[2, True, False, True, False],[2, True, False, True, False]],
  [[2, False, False, True, False],[2, True, True, False, False],[2, True, False, False, True],[2, False, True, False, False]],
]

"""0 = sortie / 1 = entrée / 2 = chemin"""


def definir_entree_sorite():
    """ Fonction qui définit l'entrée et la sortie du labyrinthe """
    entree = random.randint(1, 4)

    """if premier_cote == 1:
        deuxieme_cote = 3
    elif premier_cote == 2:
        deuxieme_cote = 4"""

    selection_sous_partie_premier_cote = random.randint(1, 5)
    """ Un côté contient 15 carrés, on divise par cinq """

    if entree == 1:
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[0][selection_carre_entree].nature = 1

            cote_sortie = random.randint(1, 4)
            if cote_sortie == 1:
                selection_carre_sortie = (13, 15)
                lab[0][selection_carre_sortie].nature = 0


        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[0][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[0][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[0][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[0][selection_carre_entree].nature = 1

    if entree == 2:
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[selection_carre_entree][0].nature = 1

        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[selection_carre_entree][0].nature = 1

        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[selection_carre_entree][0].nature = 1

        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[selection_carre_entree][0].nature = 1

        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[selection_carre_entree][0].nature = 1

    if entree == 3:
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[14][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[14][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[14][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[14][selection_carre_entree].nature = 1

        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[14][selection_carre_entree].nature = 1

    if entree == 4:
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[selection_carre_entree][14].nature = 1

        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[selection_carre_entree][14].nature = 1

        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[selection_carre_entree][14].nature = 1

        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[selection_carre_entree][14].nature = 1

        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[selection_carre_entree][14].nature = 1
