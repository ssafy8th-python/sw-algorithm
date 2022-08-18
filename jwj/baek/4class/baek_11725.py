import sys
input = sys.stdin.readline

def dfs(v):
    stack = [v]
    visited[v] = True

    while stack:
        v = stack.pop()

        for w in graph[v]:
            if not visited[w]:
                parent_node[w] = v
                stack.append(w)
                visited[w] = True


N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
parent_node = [0] * (N+1)

dfs(1)

for i in parent_node[2:]:
    print(i)
