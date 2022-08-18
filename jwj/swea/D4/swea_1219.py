def dfs(v):
    stack = [v]
    visited[v] = True

    while stack:
        v = stack.pop()

        for w in graph[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] = True

                if w == 99:
                    return 1
    return 0


for tc in range(1, 11):
    test_case, N = map(int, input().split())
    graph = [[] for _ in range(100)]

    lst = list(map(int, input().split()))

    for idx in range(0, N*2, 2):
        graph[lst[idx]].append(lst[idx+1])

    visited = [False] * 100
    result = dfs(0)

    print(f'#{tc} {result}')
