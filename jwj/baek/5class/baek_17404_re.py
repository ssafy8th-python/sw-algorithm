N = int(input())

colors = [list(map(int, input().split())) for _ in range(N)]

result = 10000000


for i in range(3):

    dp = [[1000, 1000, 1000] * 3 for _ in range(N)]
    dp[0][i] = colors[0][i]

    for idx in range(1, N):
        # red
        dp[idx][0] = colors[idx][0] + min(dp[idx - 1][1], dp[idx - 1][2])

        # green
        dp[idx][1] = colors[idx][1] + min(dp[idx - 1][0], dp[idx - 1][2])

        # blue
        dp[idx][2] = colors[idx][2] + min(dp[idx - 1][0], dp[idx - 1][1])

    for j in range(3):
        if i != j:
            if result > dp[-1][j]:
                result = dp[-1][j]
print(result)
