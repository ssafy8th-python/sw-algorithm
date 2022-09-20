import heapq, sys

input = sys.stdin.readline

INF = 10000000


def dijkstra(start, distance):
    distance[start] = 0
    visited = [False] * (N + 1)
    visited[start] = True

    q = []

    for e, w in graph[start]:
        distance[e] = w
        heapq.heappush(q, (w, e))

    while q:
        weight, node = heapq.heappop(q)

        if visited[node]:
            continue

        visited[node] = True

        for e, w in graph[node]:
            if distance[e] == INF:
                distance[e] = w + weight
            else:
                distance[e] = min(w+weight, distance[e])

            heapq.heappush(q, (distance[e], e))


N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    graph[e].append((s, w))

first, second = map(int, input().split())

result1 = 0
result2 = 0

distance = [INF] * (N + 1)
dijkstra(1, distance)
result1 += distance[first]
result2 += distance[second]

distance_first = [INF] * (N + 1)
dijkstra(first, distance_first)
result1 += distance_first[second]

distance_second = [INF] * (N + 1)
dijkstra(second, distance_second)
result2 += distance_second[first]

result1 += distance_second[N]
result2 += distance_first[N]

result = min(result1, result2)

if result >= INF:
    print(-1)
else:
    print(result)
