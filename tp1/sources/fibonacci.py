import time
import os


# Fibonacci


def fiboRec(n):
    if n <= 1:
        return 1
    return fiboRec(n - 1) + fiboRec(n - 2)


def fiboIte(n):
    tab = [1, 1]
    for i in range(2, n + 1):
        tab.append(tab[i - 1] + tab[i - 2])
    return tab[n]


class MatrixFibonacci:
    Q = [[1, 1],
         [1, 0]]

    def __init__(self):
        self.__memo = {}

    def __multiply_matrices(self, M1, M2):
        """Matrices miltiplication
        (the matrices are expected in the form of a list of 2x2 size)."""

        a11 = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
        a12 = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
        a21 = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
        a22 = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
        r = [[a11, a12], [a21, a22]]
        return r

    def __get_matrix_power(self, M, p):
        """Matrix exponentiation (it is expected that p that is equal to the power of 2)."""

        if p == 1:
            return M
        if p in self.__memo:
            return self.__memo[p]
        K = self.__get_matrix_power(M, int(p / 2))
        R = self.__multiply_matrices(K, K)
        self.__memo[p] = R
        return R

    def get_number(self, n):
        """Getting the nth Fibonacci number
        (a non-negative integer number is expected as n)."""
        if n == 0:
            return 0
        if n == 1:
            return 1
        # Factoring down the passed power into the powers that are equal to the power of 2),
        # i.e. 62 = 2^5 + 2^4 + 2^3 + 2^2 + 2^0 = 32 + 16 + 8 + 4 + 1.
        powers = [int(pow(2, b))
                  for (b, d) in enumerate(reversed(bin(n - 1)[2:])) if d == '1']
        # The same, but less pythonic: http://pastebin.com/h8cKDkHX

        matrices = [self.__get_matrix_power(MatrixFibonacci.Q, p)
                    for p in powers]
        while len(matrices) > 1:
            M1 = matrices.pop()
            M2 = matrices.pop()
            R = self.__multiply_matrices(M1, M2)
            matrices.append(R)
        return matrices[0][0][0]


# Interface Utilisateur
print("Suite de Fibonacci")
alive = True
while alive:
    print("Quel algorithme voulez vous tester ?\n0 - Quitter\n1 - Iteratif\n2 - Recursif\n3 - Logarithmique\n4 - Tous")
    choix = int(input())
    a = 0

    if choix:
        print("Pour quelle valeur ?")
        a = int(input())

    if choix == 1 or choix == 4:
        now2 = time.time()
        fiboIte(a)
        new2 = time.time() - now2
        print("Iteratif : " + str(new2))

    if choix == 3 or choix == 4:
        mfib = MatrixFibonacci()
        now = time.time()
        mfib.get_number(a)
        new = time.time() - now
        print("Logaritmique : " + str(new))

    if choix == 2 or choix == 4:
        now3 = time.time()
        fiboRec(a)
        new3 = time.time() - now3
        print("Recursif : " + str(new3))

    if choix == 0:
        alive = False

os.system("pause")
