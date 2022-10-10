import sys
import heapq

INF = int(1e9)

input = sys.stdin.readline

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    q = []

    for e, w in bus[start]:
        heapq.heappush(q, (w, e))
        distance[e] = w


    while q:
        weight, start = heapq.heappop(q)
        
        if distance[start] < weight:
            continue

        visited[start] = True

        for e, w in bus[start]:
            if not visited[e] and distance[e] > weight + w:
                distance[e] =  weight + w
                result[e] = start
                heapq.heappush(q, (distance[e], e))


n = int(input())
m = int(input())

bus = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    bus[s].append((e, w))

start, end = map(int, input().split())

visited = [False] * (n + 1)
distance = [INF] * (n + 1)
result = [start] * (n + 1)

dijkstra(start)

tmp_lst = [end]
tmp = end

while tmp != start:
    tmp_lst.append(result[tmp])
    tmp = result[tmp]

tmp_lst.reverse()

print(distance[end])
print(len(tmp_lst))
print(*tmp_lst)