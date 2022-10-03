# N과 M(9)
def comb(k):
    global tmp
    if k == M:
        tmp.add(tuple(result[::]))
        return

    for i in range(N):
        if visited[i]:
            result[k] = lst[i]
            visited[i] = False
            comb(k+1)
            visited[i] = True

N, M = map(int, input().split())
lst = list(map(int, input().split()))
result = [-1]*M
visited = [True]*N
tmp = set()
comb(0)
for elem in sorted(list(tmp)):
    print(*elem)