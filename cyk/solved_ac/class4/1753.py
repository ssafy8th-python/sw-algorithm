# 최단경로
# 인접리스트를 이용한 다익스트라 알고리즘
import sys, heapq
input = sys.stdin.readline
INF = 1e9
def dijk(start):
    q = []
    D = [INF]*(V+1)
    heapq.heappush(q, (0, start))
    D[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist: continue
        for x in G[now]:
            new_dist = dist + x[1]
            if new_dist < D[x[0]]:
                D[x[0]] = new_dist
                heapq.heappush(q,(new_dist, x[0]))

    for i in range(1, V+1):
        if D[i] == INF:
            print('INF')
        else:
            print(D[i])

V, E = map(int, input().split())
start = int(input())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v,w))

dijk(start)