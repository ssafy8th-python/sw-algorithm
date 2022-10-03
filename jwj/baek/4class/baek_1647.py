import heapq


def prim():
    q = []
    U = [False] * (N+1)
    D = []
    q.append((0, 1))

    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]:
            continue

        D.append(cost)
        U[curV] = True

        for next_node, next_cost in G[curV]:
            heapq.heappush(q, (next_cost, next_node))


    return sum(D) - max(D)


N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(M):
    n1, n2, w = map(int, input().split())
    G[n1].append((n2, w))
    G[n2].append((n1, w))

print(prim())