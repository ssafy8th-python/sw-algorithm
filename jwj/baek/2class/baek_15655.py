def comb(n, r, s):
    if r == 0:
        res.append(sorted(tmp[:]))
    else:
        for i in range(s, n - r + 1):
            tmp[r-1] = lst[i]
            comb(n, r-1, i+1)


N, M = map(int, input().split())

lst = list(map(int, input().split()))

tmp = [0] * M

res = []

comb(N, M, 0)
res.sort()

for r in res:
    print(*r)
