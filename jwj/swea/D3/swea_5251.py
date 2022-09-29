import heapq

T = int(input())

INF = 10000


def dijkstra():
    U = [False] * (N+1)
    D = [INF] * (N+1)
    D[0] = 0
    q = []
    heapq.heappush(q, (0, 0))

    while q:
        weight, curV = heapq.heappop(q)

        if U[curV]:
            continue

        U[curV] = True

        for i in range(N+1):
            if U[i]:
                continue
            if G[curV][i] and D[i] > G[curV][i] + weight:
                D[i] = G[curV][i] + weight
                heapq.heappush(q, (D[i], i))

    return D[-1]


for test_case in range(1, T+1):
    N, E = map(int, input().split())

    G = [[0] * (N+1) for _ in range(N+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w

    print(f'#{test_case} {dijkstra()}')