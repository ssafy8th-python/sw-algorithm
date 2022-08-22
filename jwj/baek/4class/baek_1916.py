from heapq import heappush, heappop
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for idx in range(M):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

distance = [100000000] * (N + 1)

start, end = map(int, input().split())
distance[start] = 0

heap = []
heappush(heap, [0, start])

while heap:
    w, v = heappop(heap)

    if distance[v] < w:
        continue

    for k, val in graph[v]:
        tmp = w + val
        if distance[k] > tmp:
            distance[k] = tmp
            heappush(heap, [tmp, k])

print(distance[end])


