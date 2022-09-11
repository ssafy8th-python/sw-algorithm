# sw-algorithm
- [DFS](#dfsdepth-first-search)


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
