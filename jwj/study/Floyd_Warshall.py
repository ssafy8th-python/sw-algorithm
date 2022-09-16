'''

    플로이드 와샬 알고리즘

    그래프에서 모든 정점 사이의 최단 거리를 구할 수 있는 알고리즘
    - BFS는 한 정점에서 모든 정점으로 최단거리를 구할 수 있음


    구혀 방법
    모든 출발점에서 경유지를 거쳐 목적지에 도착하는 값을 작은 값으로 변경하며 알고리즘을 갱신합니다.
'''

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