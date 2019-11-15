import time


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


now = time.time()
eratosthene((10 ** 7)*4)
new = time.time() - now
print(new)
