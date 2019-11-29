import random


def couples(L):
    L2 = []
    for a in L:
        for b in L:
            if a != b:
                L2.append([a, b])
    return L2


def pn_moins_un(couple):
    L = []
    if couple[0] - couple[1] > 0:
        L.append([couple[0] - couple[1], str("" + str(couple[0]) + "-" + str(couple[1]))])

    L.append([couple[0] + couple[1], str("" + str(couple[0]) + "+" + str(couple[1]))])
    L.append([couple[0] * couple[1], str("" + str(couple[0]) + "*" + str(couple[1]))])
    if couple[0] % couple[1] == 0:
        L.append([int(couple[0] / couple[1]), str("" + str(couple[0]) + "/" + str(couple[1]))])
    return L


def atteignable(L, r):
    L2 = pn_moins_un(L)
    for i in range(len(L2)):
        if r == L2[i][0]:
            print(L2[i][1])
            return True

    return False


def plaques():
    L = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]
    L2 = []

    for j in range(6):
        i = random.randint(0, len(L) - 1)
        L2.append(L[i])
        L.remove(L[i])

    return L2


def R():
    return random.randint(100, 999)


def possible(Plaques, r):
    for a in couples(Plaques):
        if atteignable(a, r):
            return True

    return False


def LCEB(pla, res):
    plaq = pla
    print(pla)

    if atteignable(pla, res):
        print("trouve")
    for c in couples(pla):
        a = pn_moins_un(c)
        if c[0] in plaq:
            plaq.remove(c[0])
        if c[1] in plaq:
            plaq.remove(c[1])

        for i in range(len(a)):

            plaq.append(a[i][0])
            if len(plaq) > 1:
                if LCEB(plaq, res):
                    print("trouve")
            else:
                if a[i][0] in plaq:
                    plaq.remove(a[i][0])
                return False
            if a[i][0] in plaq:
                plaq.remove(a[i][0])


# Affichage Utilisateur
print("Probleme non resolu, mais certaines fonctions fonctionnent")
alive = True
while alive:
    print(
        "Que faire ?\n0 - Quitter\n1 - Construire des couples\n2 - Construire Pn-1\n3 - Generer les plaques et le "
        "resultat")
    choix = int(input())
    if choix == 1:
        p = plaques()
        print("Couples possibles a partir de " + str(p) + " :\n")
        print(couples(p))
    if choix == 2:
        p = [10, 20, 30, 40]
        print("Pn-1 a partir de " + str(p) + " :\n")
        for a in couples(p):
            print(pn_moins_un(a))
    if choix == 3:
        print("Plaques generees aleatoirement :")
        print(str(plaques()) + "\n")
        print("Resultat genere aleatoirement :")
        print(str(R()) + "\n")
    if choix == 0:
        alive = False
