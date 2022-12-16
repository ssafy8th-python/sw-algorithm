from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]

parent = [0] * (N + 1)
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())

    G[a].append(b)
    parent[b] += 1

q = deque()

for i in range(1, N + 1):
    if parent[i] == 0:
        q.append(i)
        visited[i] = 1

while q:
    child = q.popleft()

    for p in G[child]:
        parent[p] -= 1

        if parent[p] == 0:
            visited[p] = visited[child] + 1
            q.append(p)

print(*visited[1:])
