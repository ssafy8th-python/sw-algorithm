T = int(input())

INF = 1000000


def dijkstra(start, G):
    U = [False] * (N + 1)
    D = [INF] * (N + 1)

    D[start] = 0

    for _ in range(N):
        minV = INF
        for i in range(1, N+1):
            if U[i]:
                continue

            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True

        for i in range(1, N+1):
            if U[i]:
                continue

            n_v = G[curV][i] + D[curV]
            if G[curV][i] and D[i] > n_v:
                D[i] = n_v

    return D


for test_case in range(1, T+1):
    N, M, X = map(int, input().split())

    G = [[0] * (N + 1) for _ in range(N+1)]
    E = [[0] * (N + 1) for _ in range(N+1)]
    for i in range(M):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        E[n2][n1] = w

    origin_lst = dijkstra(X, G)
    target_lst = dijkstra(X, E)
    maxV = 0

    for i in range(1, N+1):
        if i == X:
            continue
        tmp = origin_lst[i] + target_lst[i]

        if maxV < tmp:
            maxV = tmp

    print(f'#{test_case} {maxV}')