# 11403 경로 찾기
# 주소: https://www.acmicpc.net/problem/11403

# 제출한 답 552ms
import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, g):
    visited = [0] * n
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        if visited[v] and v == g:
            results[s][g] = 1
            return
        for i in nodes[v]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    return


n = int(input())
nodes = [[] for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            nodes[i].append(j)


results = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        bfs(i, j)

for result in results:
    print(*result)


# 수정한 답 3048ms
import sys
from collections import deque
input = sys.stdin.readline


def bfs(s, g):
    visited = [0] * n
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        if visited[v] and v == g:
            results[s][g] = 1
            return
        for i in range(n):
            if graph[v][i] and not visited[i]:
                visited[i] = 1
                q.append(i)
    return


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

results = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        bfs(i, j)

for result in results:
    print(*result)


# 다른 답
import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**7)


def dfs(v):
    for i in range(N):
        if visited[i] == 0 and graph[v][i] == 1:
            visited[i] = 1
            dfs(i)


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


for i in range(N):
    visited = [0] * N
    dfs(i)
    print(" ".join(map(str, visited)))
