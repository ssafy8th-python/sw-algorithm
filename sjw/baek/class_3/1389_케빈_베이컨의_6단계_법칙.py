# 1389 케빈 베이컨의 6단계 법칙
# 주소: https://www.acmicpc.net/problem/1389

# 제출한 답
import sys
input = sys.stdin.readline
from collections import deque


def dfs(s):
    visited = [-1] * (N + 1)
    q = deque()
    q.append(s)
    visited[s] = 0
    while q:
        v = q.popleft()
        for w in G[v]:
            if visited[w] == -1:
                q.append(w)
                visited[w] = visited[v] + 1

    return sum(visited) + 1


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

minV = 1000
result = 0
for i in range(1, N):
    tmp = dfs(i)
    if minV > tmp:
        minV = tmp
        result = i

print(result)
