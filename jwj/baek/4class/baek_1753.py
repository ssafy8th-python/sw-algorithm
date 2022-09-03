
import sys
input = sys.stdin.readline

inf = 2000000000

def smalle_node():
    minV = inf
    index = 1
    for i in range(1, V+1):
        if distance[i] < minV  and not visited[i]:
            minV = distance[i]
            index = i
    return index


def dijakstra(node_num):
    distance[start] = 0
    visited[start] = True

    for t, w in graph[start]:
        if distance[t] > w:
            distance[t] = w

    for _ in range(node_num-1):
        now = smalle_node()
        visited[now] = True

        for target, weight in graph[now]:
            tmp = weight + distance[now]
            if distance[target] > tmp:
                distance[target] = tmp


V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

distance = [inf] * (V + 1)

visited = [False] * (V + 1)

dijakstra(V)

for result in distance[1:]:
    if result == inf:
        print('INF')
    else:
        print(result)