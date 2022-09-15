
n = int(input())        # 노드의 수

m = int(input())        # 간선의 수

graph = [[] for _ in range(n + 1)]

INF = int(1e9)

distance = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    distance[i][i] = 0

for _ in range(m):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))
    distance[start][end] = min(distance[start][end], weight)

# 경유지
for m in range(1, n+1):
    # 출발지
    for s in range(1, n + 1):
        # 도착지
        for e in range(1, n + 1):
            distance[s][e] = min(distance[s][e], distance[s][m] + distance[m][e])

for i in distance[1:]:
    for j in i[1:]:
        print(j, end=" ")
    print()