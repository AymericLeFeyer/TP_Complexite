import time

# Fibonacci


def fiboRec(n):
    if n <= 1:
        return 1
    return fiboRec(n - 1) + fiboRec(n - 2)


def fiboIte(n):
    tab = [1, 1]
    for i in range (2, n+1):
        tab.append(tab[i - 1] + tab[i - 2])
    return tab[n]


def fiboLog(n):

    pass


a = 34

now = time.time()
fiboRec(a)
new = time.time() - now
print(new)

now = time.time()
fiboIte(a)
new = time.time() - now
print(new)