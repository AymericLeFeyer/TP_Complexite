import random
import time


def tri_selection(tableau):
    nb = len(tableau)
    for en_cours in range(0, nb):
        plus_petit = en_cours
        for j in range(en_cours + 1, nb):
            if tableau[j] < tableau[plus_petit]:
                plus_petit = j
        if min is not en_cours:
            temp = tableau[en_cours]
            tableau[en_cours] = tableau[plus_petit]
            tableau[plus_petit] = temp


def tri_insertion(tableau):
    for i in range(1, len(tableau)):
        en_cours = tableau[i]
        j = i
        # décalage des éléments du tableau }
        while j > 0 and tableau[j - 1] > en_cours:
            tableau[j] = tableau[j - 1]
            j = j - 1
        # on insère l'élément à sa place
        tableau[j] = en_cours


def tri_bulle(tableau):
    permutation = True
    passage = 0
    while permutation:
        permutation = False
        passage = passage + 1
        for en_cours in range(0, len(tableau) - passage):
            if tableau[en_cours] > tableau[en_cours + 1]:
                permutation = True
                # On echange les deux elements
                tableau[en_cours], tableau[en_cours + 1] = \
                    tableau[en_cours + 1], tableau[en_cours]
    return tableau


def merge(left, right):
    if not len(left) or not len(right):
        return left or right
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result


def mergesort(list):
    if len(list) < 2:
        return list
    middle = len(list) / 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


def creerTableau(n):
    T = []
    for i in range(n):
        T.append(random.randint(1, 999))
    return T


def mesurerTemps(fonction, t):
    now = time.time()
    fonction(t)
    new = time.time() - now
    print(str(fonction) + ' : ' + str(new))


mesurerTemps(tri_selection, creerTableau(10000))
mesurerTemps(tri_insertion, creerTableau(10000))
mesurerTemps(tri_bulle, creerTableau(10000))
# mesurerTemps(mergesort, creerTableau(100))
