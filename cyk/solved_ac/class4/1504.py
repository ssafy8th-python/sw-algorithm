# 특정한 최단 경로
import sys, heapq
input = sys.stdin.readline
INF = 1e9


def dijk(start, end):
    q = []
    D = [INF]*(N+1)
    heapq.heappush(q, (0, start))
    D[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if D[now] < dist: continue
        for x in G[now]:
            new_dist = dist + x[1]
            if new_dist < D[x[0]]:
                D[x[0]] = new_dist
                heapq.heappush(q, (new_dist, x[0]))
        if now == end:
            break
    return D[end]

N, E = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    G[a].append((b,c))
    G[b].append((a,c))

v1, v2 = map(int, input().split())

res1, res2, res3 = dijk(1, v1) , dijk(v1, v2),  dijk(v2, N)
res4, res5, res6 = dijk(1, v2) , dijk(v2, v1),  dijk(v1, N)


r1 = res1+res2+res3
r2 = res4+res5+res6

if min(r1,r2) >= INF:
    print(-1)
else:
    print(min(r1,r2))