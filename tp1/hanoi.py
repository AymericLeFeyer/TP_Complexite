import time


# Hanoi
def hanoi(n, a=1, b=2, c=3):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print("Deplace ", a, "sur ", c)
        hanoi(n - 1, b, a, c)


now = time.time()
hanoi(10)
new = time.time() - now
print(new)