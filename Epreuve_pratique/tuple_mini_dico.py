dictionnaire = {"ethan": 5, "noe": -3, "clement": 1, "youssef": 10}

def tuple_mini_dico(dico):
    """
    Renvoie le couple (clé valeur) associé à la valeur minimale
    apparaissant dans le tableau.
    Dans le dictionnaire dico, les valeurs sont toutes uniques.

    :param dico: dictionnaire dans lequel on recherche le tuple
    :rtype dico: dict
    :rtype tuple(str, int)

    >>> d = {"ethan": 5, "noe": -3, "clement": 1, "youssef": 10}
    >>> tuple_mini_dico(d)
    ('noe', -3)
    """
    assert len(dico) > 0

    tuple_min = ('', float('inf'))

    for cle in dico:
        if dico[cle] <= tuple_min[1]:
            tuple_min = (cle, dico[cle])
    return tuple_min

print(tuple_mni_dico(dictionnaire))

if __name__ == "__main__":
    import doctest
    doctest.testmod()