# 12865 평범한 배낭
# 주소: https://www.acmicpc.net/problem/12865

# 제출한 답
# import sys
# input = sys.stdin.readline
#
# N, K = map(int, input().split())
# things = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
# dp = [[0] * (K + 1) for _ in range(N + 1)]
#
# for n in range(1, N + 1):
#     w, v = things[n]
#     for k in range(1, K + 1):
#         if w > k:
#             dp[n][k] = dp[n - 1][k]
#         else:
#             dp[n][k] = max(dp[n - 1][k], v + dp[n - 1][k - w])
#
# print(dp[N][K])

# 다른 답
N, K = map(int, input().split())
dp = [0] * (K + 1)

for _ in range(N):
    w, v = map(int, input().split())
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

print(dp[K])