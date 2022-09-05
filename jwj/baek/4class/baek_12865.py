import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bag = [list(map(int, input().split())) for _ in range(N)]

# 냅색 알고리즘 0-1 배낭 문제

dp = [[0] * (K+1) for _ in range(N)]

for w in range(1, K+1):
    if bag[0][0] <= w:
        dp[0][w] = bag[0][1]

for idx, item in enumerate(bag[1:], 1):
    for weight in range(1, K+1):
        value = 0
        if weight >= item[0]:
            value += item[1] + dp[idx-1][weight - item[0]]

        dp[idx][weight] = max(value, dp[idx-1][weight])

print(dp[-1][-1])
