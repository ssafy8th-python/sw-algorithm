import sys, heapq
input = sys.stdin.readline

def dijkstra(start, G):
    U = [False] * (N+1)
    D = [0] * (N+1)
    q = [(0, start)]

    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]:
            continue

        U[curV] = True
        D[curV] = cost

        for newV, newC in G[curV]:
            heapq.heappush(q, (cost + newC, newV))

    return D


N, M, X = map(int, input().split())
go_lst = [[] for _ in range(N+1)]
home_lst = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, T = map(int, input().split())
    go_lst[B].append((A, T))
    home_lst[A].append((B, T))

go = dijkstra(X, go_lst)
home = dijkstra(X, home_lst)

maxV = 0

for i in range(1, N+1):
    newV = go[i] + home[i]
    if maxV < newV:
        maxV = newV

print(maxV)