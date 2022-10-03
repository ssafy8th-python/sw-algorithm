import sys, heapq
input = sys.stdin.readline

# 최소 스패닝 트리
def prim():
    U = [False] * (V+1)
    q = [(0, 1)]
    D = []
    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]:
            continue

        U[curV] = True
        D.append(cost)

        for curCost, curNode in G[curV]:
            heapq.heappush(q, (curCost, curNode))

    print(sum(D[1:]))


V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    n1, n2, w = map(int, input().split())
    G[n1].append((w, n2))
    G[n2].append((w, n1))

prim()