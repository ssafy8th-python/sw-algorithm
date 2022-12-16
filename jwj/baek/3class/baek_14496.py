from collections import deque

a, b = map(int, input().split())

N, M = map(int, input().split())

G = [set() for _ in range(N+1)]

visited = [False] * (N + 1)
q = deque()
q.append((a, 0))

for _ in range(M):
    n, m = map(int, input().split())
    G[n].add(m)
    G[m].add(n)

while q:
    node, cnt = q.popleft()

    if node == b:
        print(cnt)
        break

    if visited[node]:
        continue

    visited[node] = True

    for v in G[node]:
        q.append((v, cnt + 1))
else:
    print(-1)
