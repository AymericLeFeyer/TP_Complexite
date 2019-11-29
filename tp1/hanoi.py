import time
import os


# Hanoi
def hanoi(n, a=1, b=2, c=3):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("Deplace ", a, "sur ", c)
        hanoi(n - 1, b, a, c)


# Interface Utilisateur
print("Hanoi")
alive = True
while alive:
    print("Pour combien de valeurs ? (0 pour quitter)")
    a = int(input())
    if a:
        now = time.time()
        hanoi(a)
        new = time.time() - now
        print("Pour " + str(a) + " valeurs :\n" + str(new))
    else:
        alive = False

os.system("pause")
