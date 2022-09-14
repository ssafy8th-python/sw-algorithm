# 계단 오르기
# 1. 계단은 한번에 한계단 or 두계단 오를 수 있음
# 2. 연속된 세 개의 계단을 모두 밟아서는 안됨 단, 시작점은 계단에 포함되지 않는다
# 3. 마지막 도착 계단은 반드시 밟아야 함
# 총 점수의 최대값 도출

import sys
input = sys.stdin.readline
n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])

