import heapq, sys
input = sys.stdin.readline


def dijkstra(start):
    U = [False] * (n+1)
    D = []
    q = [(0, start)]

    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]:
            continue

        U[curV] = True
        D.append(cost)

        for newV, newC in G[curV]:
            heapq.heappush(q, (newC + cost, newV))

    print(len(D), max(D))


T = int(input())

for test_case in range(1, T+1):
    n, d, c = map(int, input().split())
    G = [[] for _ in range(n+1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        G[b].append((a, s))

    dijkstra(c)