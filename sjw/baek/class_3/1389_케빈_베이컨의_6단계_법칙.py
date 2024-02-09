# 1389 케빈 베이컨의 6단계 법칙
# 주소: https://www.acmicpc.net/problem/1389

# 제출한 답
# import sys
# input = sys.stdin.readline
# from collections import deque
#
#
# N, M = map(int, input().split())
# G = [[0] * (N + 1) for _ in range(N + 1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     G[a][b], G[b][a] = True, True
#
# sumV = [0] * (N + 1)
#
# for a in range(1, N + 1):
#     q = deque([a])
#     visited = [0] * (N + 1)
#     while q:
#         v = q.popleft()
#         for b in range(1, N + 1):
#             if G[v][b] and not visited[b]:
#                 visited[b] = visited[v] + 1
#                 q.append(b)
#
#     sumV[a] = sum(visited) - visited[a]
#
# minV = 1e10
# answer = 0
# for i in range(1, N + 1):
#     if sumV[i] < minV:
#         minV = sumV[i]
#         answer = i
#
# print(answer)


# 제출한 답2
import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b], G[b][a] = 1, 1

minV = 1e10
answer = 0
sumV = [0] * (N + 1)
for a in range(1, N + 1):
    q = deque([a])
    visited = [0] * (N + 1)
    visited[a] = 1
    while q:
        v = q.popleft()
        for b in range(1, N + 1):
            if G[v][b] and not visited[b]:
                visited[b] = visited[v] + 1
                q.append(b)

    sumV[a] = sum(visited)
    if sumV[a] < minV:
        minV = sumV[a]
        answer = a

print(answer)



# 다른 답
# from collections import deque
#
# n, m = map(int, input().split())
# arr = [[] for _ in range(n + 1)]
#
#
# def bfs(v):
#     queue = deque([v])
#     visited[v] = 1
#
#     while queue:
#         target = queue.popleft()
#         for i in arr[target]:
#             if visited[i] == 0:
#                 visited[i] = visited[target] + 1
#                 queue.append(i)
#     print(visited)
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     arr[a].append(b)
#     arr[b].append(a)
#
# res = []
#
# for i in range(1, n + 1):
#     visited = [0] * (n + 1)
#     bfs(i)
#     res.append(sum(visited))
#
# print(res.index(min(res)) + 1)
