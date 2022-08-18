import sys
imput = sys.stdin.readline

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * i for i in range(1, N+1)]

dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i):
        if dp[i][j] < dp[i-1][j] + triangle[i][j]:
            dp[i][j] = dp[i-1][j] + triangle[i][j]

        if dp[i][j+1] < dp[i-1][j] + triangle[i][j+1]:
            dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]

maxV = 0

for num in dp[N-1]:
    if maxV < num:
        maxV = num

print(maxV)
