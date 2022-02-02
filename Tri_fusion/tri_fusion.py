import doctest

def tri_fusion(tab):
    longueur = len(tab)
    if longueur == 0: return tab
    tab_gauche = tab[: longueur // 2]
    tab_droit = tab[longueur // 2:]
    return fusion(tri_fusion(tab_gauche), 
                  tri_fusion(tab_droit))
 

def fusion(tab1, tab2):
    """
    >>> fusion([5, 7], [2, 3])
    [2, 3, 5, 7]
    >>> fusion([5, 7], [5])
    [5, 5, 7]
    >>> fusion([0, 2, 4, 6, 8], [1, 3, 5, 7, 9])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    tab_final = []
    indg = indd = 0
    while indg < len(tab1) and indd < len(tab2):
        if tab1[indg] < tab2[indd]:
            tab_final.append(tab1[indg])
            indg += 1
        elif tab1[indg] > tab2[indd]:
            tab_final.append(tab2[indd])
            indd += 1
        else:
            tab_final += [tab1[indg]] * 2
            indg += 1 
            indd += 1
    # on ajoute le reste des éléments non parcourus
    # donc possiblement des tableaux vides
    tab_final += tab1[indg:] + tab2[indd:]
    return tab_final
            
fusion([1, 2, 0], [6, 5, 3])
doctest.testmod()
