import sys

sys.stdin = open("input_5102.txt", "r")

def bfs(s, g):
    q = []
    visited = [0] * (v + 1)
    q.append(s)
    visited[s] = 1
    while q:
        s = q.pop(0)
        if s == g:
            return visited[s] -1
        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[s] + 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    s, g = map(int, input().split())

    print(f'#{tc} {bfs(s, g)}')

