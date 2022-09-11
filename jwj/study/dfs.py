'''
    정점 간선
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''


'''
stack을 이용해 백트래킹 하는 방법
'''

#
# def dfs(v):
#     stack = [v]
#     visited[v] = True
#     print(v)
#     while stack:
#
#         for w in graph[v]:
#             if not visited[w]:
#                 print(w)
#                 stack.append(v)
#                 v = w
#                 visited[v] = True
#                 break
#         else:
#             v = stack.pop()
#
#
# N, M = map(int, input().split())        # 정점, 간선
#
# graph = [[] for _ in range(N + 1)]          # 정점의 수 만큼 생성
#
#
# for _ in range(M):                      # 간선 수 만큼 진행
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)
#
#
# visited = [False] * (N + 1)
# dfs(1)

'''
stack을 이용해 방문하지 않은 곳 방문 하기
'''
# def dfs(v):
#     stack = [v]
#     visited[v] = True
#     while stack:
#         v = stack.pop()
#         print(v+1)
#
#         for w in graph[v]:
#             if not visited[w]:
#                 stack.append(w)
#                 visited[w] = True

'''
재귀를 이용 하는 방법
'''


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
