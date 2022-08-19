import sys
input = sys.stdin.readline

N = int(input())

dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(3):
        tmp1 = dp[i][j] + dp[i-1][j-1]
        tmp2 = dp[i][j] + dp[i-1][j-2]

        dp[i][j] = min(tmp1, tmp2)

print(min(dp[N-1]))
