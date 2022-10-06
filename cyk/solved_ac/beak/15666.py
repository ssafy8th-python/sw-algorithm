# N과 M(12)
def perm(k, s):
    if k == M:
        tmp.add(tuple(result[::]))
        return
    for i in range(s, N):
        result[k] = lst[i]
        perm(k+1, i)

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = [-1]*M
tmp = set()
perm(0,0)

for lst in sorted(list(tmp)):
    print(*lst)