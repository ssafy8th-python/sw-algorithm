# 케빈 베이컨의 6단계 법칙 성공
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
def bfs(v):
    visited = [0] *(N+1)
    visited[v] = 1
    q = []
    q.append(v)
    while q:
        v = q.pop(0)
        for w in arr[v]:
            if visited[w] == 0:
                visited[w] = visited[v]+1
                q.append(w)
    return visited
for _ in range(M):
    par, chd = map(int, input().split())
    arr[par].append(chd)
    arr[chd].append(par)
res = 10000000
temp=[] 
for i in range(1, N+1):
    if res > sum(bfs(i))-N:
        res = sum(bfs(i))-N
        temp = i
print(temp)
