'''
    정점 간선
7 8
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

visited = [False] * (N+1)
que = [1]
visited[1] = True

distance = [0] * (N+1)
distance[1] = 1

while que:
    v = que.pop(0)

    print(v)

    for w in graph[v]:
        # if not visited[w]:
        if not distance[w]:
            visited[w] = True
            distance[w] = distance[v] + 1   # 거리를 측정할 수 있음
            que.append(w)


print(distance[1:])