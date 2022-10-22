import sys
input = sys.stdin.readline

dir_lst = [
    [0, 2, 2, 2, 2],
    [0, 1, 3, 4, 3],
    [0, 3, 1, 3, 4],
    [0, 4, 3, 1, 3],
    [0, 3, 4, 3, 1],
]


direction = list(map(int, input().split()))

dp = [[[400000] * 5 for _ in range(5)] for _ in range(len(direction) + 1)]

dp[-1][0][0] = 0

for move in range(len(direction) - 1):
    for left in range(5):
        for right in range(5):
            dp[move][direction[move]][right] = min(dp[move][direction[move]][right],
                                                   dp[move-1][left][right] + dir_lst[left][direction[move]])

            dp[move][left][direction[move]] = min(dp[move][left][direction[move]],
                                                   dp[move-1][left][right] + dir_lst[right][direction[move]])

result = 400000
for i in range(5):
    for j in range(5):
        result = min(result, dp[len(direction) - 2][i][j])

print(result)

