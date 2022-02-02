def tri_fusion(tab, cmp=lambda x, y: x < y):
    longueur = len(tab)
    if longueur == 0: return tab
    tab_gauche = tab[: longueur // 2]
    tab_droit = tab[longueur // 2:]
    return _fusion(tri_fusion(tab_gauche, cmp), 
                  tri_fusion(tab_droit, cmp), 
                 cmp)
 

def _fusion(tab1, tab2, cmp):
    tab_final = []
    indg = indd = 0
    while indg < len(tab1) and indd < len(tab2):
        if cmp(tab1[indg], tab2[indd]):
            tab_final.append(tab1[indg])
            indg += 1
        else:
            tab_final.append(tab2[indd])
            indd += 1
            
    # on ajoute le reste des éléments non parcourus
    # donc possiblement des tableaux vides
    tab_final += tab1[indg:] + tab2[indd:]
    return tab_final
            
def est_plus_grand_que(x, y):
    return x > y

tri_fusion([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], cmp=est_plus_grand_que)
