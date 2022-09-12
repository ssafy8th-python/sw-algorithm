# sw-algorithm
- [DFS](#dfsdepth-first-search)
- [Dijkstra](#dijkstra)
- [Bellman-Ford](#bellman-ford)

## DFS(Depth First Search)

### 사용되는 문제 유형
- 모든 정점을 방문하는 경우
- 각각의 경로마다 특징을 저장해야하는 경우

### 구현 방법
- 스택
```

def dfs(v):
    stack = [v]
    visited[v] = True
    print(v)
    while stack:

        for w in graph[v]:
            if not visited[w]:
                print(w)                # 방문한 노드를 출력
                stack.append(v)
                v = w
                visited[v] = True
                break
        else:
            v = stack.pop()             # 방문할 수 있는 노드가 없다면 백트래킹


N, M = map(int, input().split())        # 정점, 간선

graph = [[] for _ in range(N + 1)]      # 정점의 수 만큼 생성


for _ in range(M):                      # 간선 수 만큼 진행
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False] * (N + 1)
dfs(1)
```

- 재귀
```
def dfs(v):
    visited[v] = True
    print(v)
    for w in graph[v]:
        if not visited[w]:
            dfs(w)


N, M = map(int, input().split())        # 정점, 간선

graph = [[] for _ in range(N + 1)]          # 정점의 수 만큼 생성


for _ in range(M):                      # 간선 수 만큼 진행
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (N + 1)

dfs(1)

```

## dijkstra

### 사용되는 문제 유형
- 특정 노드에서 출발하여 각각의 노드에 최단경로를 구하는 경우
- 양수에 해당하는 가중치만 포함하는 경우
- 네비게이션 문제

### 구현 방법
- 단순 구현하는 방법
1. 최단 거리의 노드를 계산한다. => get_samllest()
2. 해당 노드에서 간선의 거리를 계산하여 작은 값으로 update를 해준다.
3. 위 1-2 방법을 노드의 수 - 1 만큼 반복한다. => 노드의 수 - 1에서 -1은 시작 값을 이미 방문 했기 때문
```
test_case = 0
INF = int(1e9)


def get_smallest():
    minV = INF
    x = y = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and minV > distance[i][j]:
                minV = distance[i][j]
                x = i
                y = j

    return x, y


def dijkstra(x, y):
    distance[x][y+1] = distance[x][y] + cave[x][y+1]
    distance[x+1][y] = distance[x][y] + cave[x+1][y]

    for _ in range(N * N - 1):
        node = get_smallest()

        visited[node[0]][node[1]] = True

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = node[0] + d_x
            n_y = node[1] + d_y

            if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y]:
                new_dist = distance[node[0]][node[1]] + cave[n_x][n_y]
                
                if distance[n_x][n_y] > new_dist :
                    distance[n_x][n_y] = new_dist

    return distance[-1][-1]


while True:
    test_case += 1

    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    distance = [[INF] * N for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    visited[0][0] = True
    distance[0][0] = cave[0][0]

    print(f"Problem {test_case}: {dijkstra(0, 0)}")



```


- heapq를 이용하는 방법
1. heapq에 거리에 해당하는 값을 push 하여 최소힙으로 저장한다.
2. 최소 값에 해당하는 값을 pop 한다.
3. 최소 값에 해당하는 node의 간선을 계산하여 update하여 heapq에 push 한다.
4. 위 1-3방법을 방문할 노드가 없어질때까지 반복한다.

```
import heapq

test_case = 0
INF = int(1e9)

def dijkstra(x, y):
    q = []

    distance[x][y+1] = distance[x][y] + cave[x][y+1]
    distance[x+1][y] = distance[x][y] + cave[x+1][y]

    heapq.heappush(q, (distance[x][y+1], x, y+1))
    heapq.heappush(q, (distance[x+1][y], x+1, y))

    while q:
        dist, i, j = heapq.heappop(q)

        visited[i][j] = True

        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = i + d_x
            n_y = j + d_y

            if 0 <= n_x < N and 0 <= n_y < N and not visited[n_x][n_y]:
                new_dist = dist + cave[n_x][n_y]

                if distance[n_x][n_y] > new_dist:
                    distance[n_x][n_y] = new_dist
                    heapq.heappush(q, (new_dist, n_x, n_y))

    return distance[-1][-1]


while True:
    test_case += 1

    N = int(input())

    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    distance = [[INF] * N for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    visited[0][0] = True
    distance[0][0] = cave[0][0]

    print(f"Problem {test_case}: {dijkstra(0, 0)}")

```

## Bellman-Ford

### 사용되는 문제 유형
- 음수 가중치를 포함하고 있는 그래프에서 최단 거리를 구하는 경우
- 음수 사이클의 존재 여부를 파악할 수 있다.


### 구현 방법
1. 시작 노드 설정
2. 각 노드의 거리 값을 무한대로 설정하고 시작노드는 0으로 설정
3. 무한대로 설정되어 있지 않은 현제 노드에서 모든 인접 노드를 탐색하여 더 짧은 거리인 경우 값을 갱신
4. 3번 과정을 모든 노드에 대해 수행
5. 노드의 수만큼 실행 했을 때 거리가 갱신된다면 음수 사이클이 존재함을 알 수 있음

```
'''
input

3 3
1 2 3
2 3 4
3 1 -8

'''

INF = int(1e9)


def bellman_ford(start):
    distance = [INF] * (V + 1)
    distance[start] = 0

    # 한번더 반복하여 값의 변화 유무에 따라 음수 싸이클인지 확인
    for i in range(V):
        for s, e, w in edges:
            if distance[s] != INF and distance[e] > distance[s] + w:
                if i == V - 1:
                    return distance

                distance[e] = distance[s] + w

    return distance


V, E = map(int, input().split())     # N = node, M = edge

edges= []

for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

res = bellman_ford(1)
print(res)

# [1000000000, -2, 2, 6]
```

