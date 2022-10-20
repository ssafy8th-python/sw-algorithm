from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for _ in range(M):
    S, E = map(int, input().split())
    G[S].append(E)
    in_degree[E] += 1

q = deque()

for i in range(1, N+1):
    if not in_degree[i]:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)

    for i in G[now]:
        in_degree[i] -= 1

        if in_degree[i] == 0:
            q.append(i)

print(*result)