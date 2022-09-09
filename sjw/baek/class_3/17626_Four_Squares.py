# 17626 Four Squares
# 주소: https://www.acmicpc.net/problem/17626

# 제출한 답
# import sys
# input = sys.stdin.readline

def check():
    d = int(n ** 0.5)

    a, b, c = 0, 0, 0

    for i in range(d, 0, -1):
        a = n - (i ** 2)
        if a == 0:
            lst.append(1)
            return
        e = int(a ** 0.5)

        for j in range(e, 0, -1):
            b = a - (j ** 2)
            if b == 0:
                lst.append(2)
                return
            f = int(b ** 0.5)

            for k in range(f, 0, -1):
                c = b - (f ** 2)
                if c == 0:
                    lst.append(3)
                    break


n = int(input())
lst = [4]


check()
print(min(lst))


# 다른 답
from math import trunc


def sqr4(sqrt1):

    if N == sqrt1 ** 2:
        return 1

    while True:
        if sqrt1 == 0:
            break
        sqrt2 = trunc((N - sqrt1 ** 2) ** (1 / 2))
        if (N - sqrt1 ** 2) == sqrt2 ** 2:
            return 2
        sqrt1 -= 1

    n = 0
    while True:
        if N < 4 ** n:
            break
        if (N / (4 ** n) - 7) % 8 == 0:
            return 4
        n += 1

    return 3


N = int(input())
sqr = trunc(N ** (1 / 2))
print(sqr4(sqr))
