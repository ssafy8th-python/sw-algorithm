# 퇴사 2
# (1 ≤ N ≤ 1,500,000)
# (1 ≤ Ti ≤ 50, 1 ≤ Pi ≤ 1,000)
import sys
input = sys.stdin.readline
N = int(input())
lst = []
mx = 0
for _ in range(N):
    lst.append(list(map(int, input().split())))
dp = [0]*(N+1)

k = 0
for i in range(N):
    k = max(k, dp[i])
    if i + lst[i][0] > N:
        continue
    dp[i+lst[i][0]] = max(k+lst[i][1], dp[i+lst[i][0]])

print(max(dp))