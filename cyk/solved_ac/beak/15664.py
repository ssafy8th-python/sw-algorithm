# N과 M(10)
def comb(k, s):
    global tmp
    if k == M:
        tmp.add(tuple(result[::]))
        return
    for i in range(s, N):
        if visited[i]:
            result[k] = lst[i]
            visited[i] = False
            comb(k+1, i)
            visited[i] = True


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = [-1]*M
visited = [True]*N
tmp = set()
comb(0,0)
for lst in sorted(list(tmp)):
    print(*lst)
