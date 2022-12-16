T = int(input())

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    n = int(input())
    res = 0
    for _ in range(n):
        tx, ty, r = map(int, input().split())

        t1 = ((x1 - tx) ** 2 + (y1 - ty) ** 2) < r ** 2

        t2 = ((x2 - tx) ** 2 + (y2 - ty) ** 2) < r ** 2

        if t1 or t2:
            res += 1

        if t1 and t2:
            res -= 1

    print(res)
