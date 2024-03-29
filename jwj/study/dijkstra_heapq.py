'''
5 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

import heapq

INF = int(1e9)


def dijk():
    U = []
    D = [INF] * (V+1)
    D[0] = 0
    P = [INF] * (V+1)

    q = []
    heapq.heappush(q, (0, 0))

    while len(U) < V + 1:
        # 가장 작은 노드를 찾음
        weight, curV = heapq.heappop(q)
        if curV in U: continue

        U.append(curV)

        # 해당 노드를 방문하는 작은 가중치로 갱신
        for i in range(V+1):
            if i in U: continue
            if G[curV][i] and D[i] > G[curV][i] + D[curV]:
                D[i] = G[curV][i] + D[curV]
                P[i] = curV
                heapq.heappush(q, (D[i], i))

    print(U, D, P)


V, E = map(int, input().split())

G = [[0] * (V+1) for _ in range(V+1)]

for i in range(E):
    n1, n2, w = map(int, input().split())
    G[n1][n2] = w

dijk()