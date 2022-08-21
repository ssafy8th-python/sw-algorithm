import sys
input = sys.stdin.readline

N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range(N+1)]
tmp = 0

for x in range(N):
    for y in range(N):
        dp[x+1][y+1] = dp[x][y+1] + dp[x+1][y] - dp[x][y] + table[x][y]


for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(dp[x2][y2] - (dp[x1-1][y2] + dp[x2][y1-1] - dp[x1-1][y1-1]))

