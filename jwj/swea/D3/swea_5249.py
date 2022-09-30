T = int(input())


def prime():
    U = [False] * (V + 1)
    D = [100] * (V + 1)
    D[0] = 0

    for _ in range(V+1):

        minV = 100
        for i in range(V+1):
            if U[i]:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i

        U[curV] = True

        for i in range(V+1):
            if U[i]:
                continue

            if G[curV][i] and D[i] > G[curV][i]:
                D[i] = G[curV][i]
    return sum(D)


for test_case in range(1, T+1):
    V, E = map(int, input().split())

    G = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w

    print(f'#{test_case} {prime()}')