# 1753 최단경로
# 주소: https://www.acmicpc.net/problem/1753

# 제출한 답
# import sys
# input = sys.stdin.readline
# import heapq
#
#
# V, E = map(int, input().split())
# K = int(input())
# G = [[] for _ in range(V + 1)]
#
# for _ in range(E):
#     u, v, w = map(int, input().split())
#     G[u].append([v, w])
#
# heap = []
# heapq.heappush(heap, [0, K])
#
# visited = [0] * (V + 1)
# distance = ['INF'] * (V + 1)
# distance[K] = 0
# while heap:
#     d, u = heapq.heappop(heap)
#     visited[u] = 1
#     for v, w in G[u]:
#         if not visited[v]:
#             if distance[v] == 'INF' or distance[v] > d + w:
#                 distance[v] = d + w
#                 heapq.heappush(heap, [distance[v], v])
#
# for answer in distance[1:]:
#     print(answer)


# 다른 답
import heapq, sys
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
edge = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    edge[u].append([v, w])

d = [1e9 for _ in range(V + 1)]
d[K] = 0
pq = [(0, K)]

while pq:
    w, node = heapq.heappop(pq)
    if d[node] >= w:
        for next_node, next_w in edge[node]:
            new_w = d[node] + next_w
            if new_w < d[next_node]:
                d[next_node] = new_w
                heapq.heappush(pq, (new_w, next_node))

for i in range(1, V + 1):
    print(d[i] if d[i] != 1e9 else "INF")
