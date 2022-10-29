# 최소비용 구하기
import sys, heapq
input = sys.stdin.readline
INF = 1e9
def dijk(s, e):
    q = []
    D = [INF] * (N+1)
    heapq.heappush(q, (0, s))
    D[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if D[now] < dist: continue
        for x in Bus[now]:
            new_dist = dist+x[1]
            if new_dist < D[x[0]]:
                D[x[0]] = new_dist
                heapq.heappush(q, (new_dist, x[0]))

        if now == end:
            break
    print(D[end])
N = int(input())
B = int(input())
Bus = [[] for _ in range(N+1)]
for _ in range(B):
    sc, ec, w = map(int, input().split())
    Bus[sc].append((ec, w))

start, end = map(int, input().split())
dijk(start, end)