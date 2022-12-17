N = int(input())

remain = 1000000000

dp = [[1] * 10 for _ in range(N)]
dp[0][0] = 0

for i in range(1, N):
    dp[i][0] = dp[i-1][1] % remain

    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] % remain

    dp[i][9] = dp[i-1][8] % remain

print(sum(dp[N-1]) % remain)
