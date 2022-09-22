def f(i, k, r):
    if i == r:
        print(p)
    else:
        for j in range(k):
            if not used[j]:
                used[j] = True
                p[i] = a[j]
                f(i+1, k, r)
                used[j] = False


N = 3
R = 3
a = [i for i in range(1, N+1)]
used = [False] * N
p = [0] * N

f(0, N, R)
