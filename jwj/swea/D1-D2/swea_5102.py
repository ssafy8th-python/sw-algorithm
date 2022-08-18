from collections import deque

T = int(input())

for tc in range(1, T+1):

    que = deque()

    V, E = map(int, input().split())

    visited = [False] * (V+1)

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, end = map(int, input().split())

    que.append((start, 0))
    minV = 50

    while que:
        v, cnt = que.popleft()
        visited[v] = True

        if v == end:
            if minV > cnt:
                minV = cnt

        for w in graph[v]:
            if not visited[w]:
                que.append((w, cnt+1))

    if minV == 50:
        minV = 0

    print(f'#{tc} {minV}')
