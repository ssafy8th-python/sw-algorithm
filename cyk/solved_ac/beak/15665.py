# N과 N(11)
def perm(k):
    if k == M:
        tmp.add(tuple(result[::]))
        return
    for i in range(N):
        result[k] = lst[i]
        perm(k+1)

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = [-1]*M
tmp = set()
perm(0)

for lst in sorted(list(tmp)):
    print(*lst)