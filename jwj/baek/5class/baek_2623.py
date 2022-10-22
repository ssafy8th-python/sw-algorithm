from collections import deque

N, M = map(int, input().split())

G = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    lst = list(map(int, input().split()))
    for i in range(2, lst[0] + 1):
        G[lst[i-1]].append(lst[i])
        in_degree[lst[i]] += 1

q = deque()

for i in range(1, N+1):
    if in_degree[i] == 0:
        q.append(i)


result = []
while q:
    now = q.popleft()
    result.append(now)

    for i in G[now]:
        in_degree[i] -= 1

        if in_degree[i] == 0:
            q.append(i)

if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)
