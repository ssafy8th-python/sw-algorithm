# BFS와 DFS
'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
def dfs(v):
    res = [v]
    stack = []
    visited[v] = True
    while True:
        for w in arr[v]:
            if not visited[w]:
                res.append(w)
                stack.append(v)
                v = w
                visited[v] = True
                break
        else:
            if stack:
                v = stack.pop()
        
        if not stack:
            break
    
    return res

def bfs(v, N):
    res = [v]
    que = [v]
    visited = [False] *(N+1)
    visited[v] = True
    while que:
        v = que.pop(0)
        for w in arr[v]:
            if not visited[w]:
                visited[w] = True
                que.append(w)
                res.append(w)
    return res


N, M, V = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    par, chd = map(int, input().split())
    arr[par].append(chd)
    arr[chd].append(par)

for i in range(1,N+1):
    arr[i].sort()

visited = [False] * (N+1)

print(*dfs(V))
print(*bfs(V, N))