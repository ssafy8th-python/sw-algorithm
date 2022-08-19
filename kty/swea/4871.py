import sys

sys.stdin = open("input_4871.txt", "r")

def dfs(graph, S, visited):
    visited[S] = True
    if S == G:
        return 1
    for i in graph[S]:
        if not visited[i]:
            if dfs(graph, i, visited) == 1:
                return 1
                
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        st, ed = list(map(int, input().split()))
        graph[st].append(ed)

    S, G = map(int, input().split())
    visited = [False] * (V + 1)
    print(f'#{tc} {dfs(graph, S, visited)}')
