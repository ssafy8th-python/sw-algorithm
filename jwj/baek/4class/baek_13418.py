import sys, heapq
input = sys.stdin.readline


def prim(G):
    U = [False] * (N + 1)
    U[0] = True
    result = 0
    q = [(G[0][0][1], 1)]

    while q:
        cost, curV = heapq.heappop(q)

        if U[curV]:
            continue

        U[curV] = True

        result += cost

        for newV, newC in G[curV]:
            heapq.heappush(q, (newC, newV))

    return result


N, M = map(int, input().split())

max_G = [[] for _ in range(N+1)]
min_G = [[] for _ in range(N+1)]

for _ in range(M+1):
    A, B, C = map(int, input().split())
    if C == 0:
        max_G[A].append((B, 0))
        max_G[B].append((A, 0))
        min_G[A].append((B, 1))
        min_G[B].append((A, 1))
    else:
        max_G[A].append((B, 1))
        max_G[B].append((A, 1))
        min_G[A].append((B, 0))
        min_G[B].append((A, 0))

a = prim(max_G)
b = prim(min_G)

a = (N - a) ** 2
b = b ** 2

print(a-b)
