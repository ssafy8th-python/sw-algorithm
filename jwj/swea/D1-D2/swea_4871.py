def dfs(v):

    stack = [v]
    visited[v] = True
    check = False

    while stack:
        v = stack.pop()

        if v == end:
            check = True
            break

        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True

    if check:
        return 1
    else:
        return 0


T = int(input())

for tc in range(1, T+1):

    V, E = map(int, input().split())

    visited = [False] * (V+1)

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)

    start, end = map(int, input().split())

    result = dfs(start)

    print(f'#{tc} {result}')


