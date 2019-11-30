import time
import os


def eratosthene(n):
    nombres, premiers = [], []
    for i in range(2, n + 1):
        nombres.append(True)
    for i in range(2, n + 1):
        if nombres[i - 2]:
            premiers.append(i)
            for j in range(2 * i, n + 1, i):
                nombres[j - 2] = False
    return premiers


print("Crible d'Eratosthene")
alive = True
while alive:
    print("Pour quelle valeur ? (0 pour quitter)")
    a = int(input())
    if a:
        now = time.time()
        eratosthene(a)
        new = time.time() - now
        print(new)
    else:
        alive = False

os.system("pause")