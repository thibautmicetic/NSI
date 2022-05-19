# Créé par tmicetic, le 19/05/2022 en Python 3.7
import doctest

def indice_max(tab):
    """ Renvoie le plus petit indice de la valeur maximale d'un tableau

    :param tab: liste d'entiers relatifs
    :type tab: list(int)
    :rtype: int

    >>> indice_max([0, 2, 5, 4, -6])
    2
    >>> indice_max([2, 2])
    0
    >>> indice_max([-4])
    0

     """
    assert len(tab) != 0

    indice = 0
    element_max = tab[0]
    for i in range(1, len(tab)):
        # < car on cherche le plus petit indice
        if element_max < tab[i]:
            element_max = tab[i]
            indice = i
    return indice

print(indice_max([2, 4, 3, 8, 5, 1]))
print(indice_max([2, 4, 9, 8, 5, 10, 7]))

print(doctest.testmod())