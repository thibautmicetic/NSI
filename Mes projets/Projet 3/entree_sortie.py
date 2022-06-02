import random
"""0 = sortie / 1 = entrée / 2 = chemin"""

def definir_entree_sorite(lab):
    """ Fonction qui définit l'entrée et la sortie du labyrinthe """

    # Sélection du côté de l'entrée
    entree = random.randint(1, 4)

    selection_sous_partie_premier_cote = random.randint(1, 5)

    # Sélection du côté de l'entrée
    if entree == 1:

        # Sélection sous partie du côté pour choisir le carré final
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[0][selection_carre_entree].nature = 1
            # Sélection du carré de la sortie selon le côté de l'entrée
            sortie = random.randint(1, 4)

            # Sélection du côté de la sortie selon l'entrée
            if sortie == 1:
                selection_carre_sortie = random.randint(11, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(8, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 2
        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[0][selection_carre_entree].nature = 1
            sortie = random.randint(2, 4)

            # Définition de la sortie
            if sortie == 2:
                selection_carre_sortie = random.randint(5, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 3
        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[0][selection_carre_entree].nature = 1
            sortie = random.randint(2, 4)

            if sortie == 2:
                selection_carre_sortie = random.randint(2, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(2, 14)
                lab[selection_carre_entree][14].nature = 0

        # Sous-partie 4
        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[0][selection_carre_entree].nature = 1
            sortie = random.randint(2, 4)

            if sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(5, 14)
                lab[selection_carre_sortie][14].nature = 0

        #Sous-partie 5
        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[0][selection_carre_entree].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 2)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(5, 14)
                lab[selection_carre_sortie][14].nature = 0

    # Entrée côté 2
    if entree == 2:
        # Sous-partie 1
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[selection_carre_entree][0].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(8, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(11, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 2
        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[selection_carre_entree][0].nature = 1
            liste_cote_sortie = [1, 3, 4]
            sortie = random.choice(liste_cote_sortie)

            if sortie == 1:
                selection_carre_sortie = random.randint(5, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 3
        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[selection_carre_entree][0].nature = 1
            liste_cote_sortie = [1, 3, 4]
            sortie = random.choice(liste_cote_sortie)

            if sortie == 1:
                selection_carre_sortie = random.randint(2, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(2, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 4
        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[selection_carre_entree][0].nature = 1
            liste_cote_sortie = [1, 3, 4]
            sortie = random.choice(liste_cote_sortie)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(5, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 5
        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[selection_carre_entree][0].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 2)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(9, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

    # Entrée côté 3
    if entree == 3:
        #Sous-partie 1
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[14][selection_carre_entree].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 5)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(11, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 2
        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[14][selection_carre_entree].nature = 1
            liste_cote_sortie = [1, 2, 4]
            sortie = random.choice(liste_cote_sortie)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 8)
                lab[selection_carre_sortie][0].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 3
        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[14][selection_carre_entree].nature = 1
            liste_cote_sortie = [1, 2, 4]
            sortie = random.choice(liste_cote_sortie)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 11)
                lab[selection_carre_sortie][0].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 11)
                lab[selection_carre_sortie][14].nature = 0


        # Sous-partie 4
        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[14][selection_carre_entree].nature = 1
            liste_cote_sortie = [1, 2, 4]
            sortie = random.choice(liste_cote_sortie)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 8)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 5
        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[14][selection_carre_entree].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 2)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 5)
                lab[selection_carre_sortie][14].nature = 0

    # Entrée côté 4
    if entree == 4:
        # Sous-partie 1
        if selection_sous_partie_premier_cote == 1:
            selection_carre_entree = random.randint(0, 2)
            lab[selection_carre_entree][14].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 5)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 2)
                lab[selection_carre_sortie][14].nature = 0

        # Sous-partie 2
        elif selection_sous_partie_premier_cote == 2:
            selection_carre_entree = random.randint(3, 5)
            lab[selection_carre_entree][14].nature = 1
            sortie = random.randint(1, 3)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 14)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 8)
                lab[14][selection_carre_sortie].nature = 0

        # Sous-partie 3
        elif selection_sous_partie_premier_cote == 3:
            selection_carre_entree = random.randint(6, 8)
            lab[selection_carre_entree][14].nature = 1
            sortie = random.randint(1, 3)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 11)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 11)
                lab[14][selection_carre_sortie].nature = 0

        # Sous-partie 4
        elif selection_sous_partie_premier_cote == 4:
            selection_carre_entree = random.randint(9, 11)
            lab[selection_carre_entree][14].nature = 1
            sortie = random.randint(1, 3)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 8)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            else:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

        # Sous-partie 5
        elif selection_sous_partie_premier_cote == 5:
            selection_carre_entree = random.randint(12, 14)
            lab[selection_carre_entree][14].nature = 1
            sortie = random.randint(1, 4)

            if sortie == 1:
                selection_carre_sortie = random.randint(0, 5)
                lab[0][selection_carre_sortie].nature = 0

            elif sortie == 2:
                selection_carre_sortie = random.randint(0, 14)
                lab[selection_carre_sortie][0].nature = 0

            elif sortie == 3:
                selection_carre_sortie = random.randint(0, 14)
                lab[14][selection_carre_sortie].nature = 0

            else:
                selection_carre_sortie = random.randint(11, 14)
                lab[selection_carre_sortie][14].nature = 0
