import sys

sys.stdin = open("input_1219.txt", "r")

def dfs(graph, S, visited):
    visited[S] = True
    if S == 99:
        return 1
    for i in graph[S]:
        if not visited[i]:
            if dfs(graph, i, visited) == 1:
                return 1
    return 0

# 정석
# v = s.pop(-1)
# print(v, end = '')
# for w in G[v]:
#     if not visited[w]:
#         if W == G:
#             return 1
#         s.append(w)
#         visited[w] = True
# return 0

T = 10
for _ in range(1, T + 1):
    tc, N = map(int, input().split())
    graph = [[] for _ in range(100)]
    num = list(map(int, input().split()))
    for i in range(0, len(num), 2):
        graph[num[i]].append(num[i+1])
    visited = [False] * 100
    print(f'#{tc} {dfs(graph, 0, visited)}')












    # graph[st].append(ed)
    # print(graph)
    # S, G = map(int, input().split())
    # visited = [False] * (V + 1)
    # print(f'#{tc} {dfs(graph, S, visited)}')
