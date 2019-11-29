import random
import time
import os


def tri_selection(tableau):
    nbe = len(tableau)
    for en_cours in range(0, nbe):
        plus_petit = en_cours
        for j in range(en_cours + 1, nbe):
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


def fusion(gauche, droite):
    resultat = []
    index_gauche, index_droite = 0, 0
    while index_gauche < len(gauche) and index_droite < len(droite):
        if gauche[index_gauche] <= droite[index_droite]:
            resultat.append(gauche[index_gauche])
            index_gauche += 1
        else:
            resultat.append(droite[index_droite])
            index_droite += 1
    if gauche:
        resultat.extend(gauche[index_gauche:])
    if droite:
        resultat.extend(droite[index_droite:])
    return resultat


def tri_fusion(m):
    if len(m) <= 1:
        return m
    milieu = len(m) // 2
    gauche = m[:milieu]
    droite = m[milieu:]
    gauche = tri_fusion(gauche)
    droite = tri_fusion(droite)
    return list(fusion(gauche, droite))


def creerTableau(n):
    T = []
    for i in range(n):
        T.append(random.randint(1, 999))
    return T


def mesurerTemps(fonction, t):
    print("Mesure du temps pour " + str(fonction))
    now = time.time()
    fonction(t)
    new = time.time() - now
    print(str(fonction) + ' : ' + str(new) + '\n')


# Affichage Utilisateur
alive = True
while alive:
    print("Quel tri voulez vous tester ?\n0 - Quitter\n1 - Selection\n2 - Insertion\n3 - Bulle\n4 - Fusion\n5 - Tous")
    whichOne = int(input())

    print("Pour combien de valeurs souhaitez vous tester les tris ?")
    nb = int(input())

    if whichOne == 1 or whichOne == 5:
        mesurerTemps(tri_selection, creerTableau(nb))
    if whichOne == 2 or whichOne == 5:
        mesurerTemps(tri_insertion, creerTableau(nb))
    if whichOne == 3 or whichOne == 5:
        mesurerTemps(tri_bulle, creerTableau(nb))
    if whichOne == 4 or whichOne == 5:
        mesurerTemps(tri_fusion, creerTableau(nb))
    if whichOne == 0:
        alive = False

os.system("pause")