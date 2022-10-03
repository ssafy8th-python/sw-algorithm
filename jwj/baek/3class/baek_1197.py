import sys, heapq
input = sys.stdin.readline

INF = 1000000
def prim():
    U = [False] * (V + 1)
    D = []
    q = []
    heapq.heappush(q, (0, 1))

    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]:
            continue

        D.append(cost)
        U[curV] = True

        for newV, newC in G[curV]:
            heapq.heappush(q, (newC, newV))

    print(sum(D))


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))


prim()