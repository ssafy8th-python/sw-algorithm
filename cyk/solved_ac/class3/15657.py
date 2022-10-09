# N과 M(8)

def comb(k, s):
    if k == M:
        print(*result)
        return
    for i in range(s, N):
        result[k] = lst[i]
        comb(k+1, i)

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = [-1]*M
comb(0, 0)