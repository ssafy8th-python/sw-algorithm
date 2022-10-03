# N과 M(6)

def comb(k, s):
    if k == M:
        print(*result)
        return
    for i in range(s, N-(M-k)+1):
        if visited[i]:
            result[k] = lst[i]
            visited[i] = False
            comb(k+1, i)
            visited[i] = True



N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
result = [-1]*M
visited = [True]*N
comb(0,0)