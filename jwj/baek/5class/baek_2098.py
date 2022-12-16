def traveling(start, visited):
    if dp[start][visited]:
        return dp[start][visited]

    if visited == (1 << N) - 1:
        if city[start][0]:
            return city[start][0]
        else:
            return INF

    dp[start][visited] = INF

    for i in range(1, N):
        if city[start][i] == 0:
            continue

        if visited & (1 << i):
            continue

        dp[start][visited] = min(dp[start][visited], traveling(i, visited | (1 << i)) + city[start][i])

    return dp[start][visited]


N = int(input())

city = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << N) for _ in range(N)]

INF = int(1e9)

print(traveling(0, 1))
