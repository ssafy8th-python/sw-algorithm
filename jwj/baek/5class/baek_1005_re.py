from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    G = [[] for _ in range(N+1)]
    P = [[] for _ in range(N+1)]
    buildings = [0] + list(map(int, input().split()))
    in_degree = [0] * (N + 1)
    dp = [0] * (N + 1)
    for _ in range(K):
        S, E = map(int, input().split())
        G[S].append(E)
        P[E].append(S)
        in_degree[E] += 1

    destination = int(input())

    q = deque()

    for i in range(1, N+1):
        if in_degree[i] == 0:
            q.append(i)
            dp[i] = buildings[i]

    while q:
        now = q.popleft()

        for i in G[now]:
            in_degree[i] -= 1
            dp[i] = max(dp[i], dp[now] + buildings[i])
            if in_degree[i] == 0:
                q.append(i)

    print(dp[destination])
