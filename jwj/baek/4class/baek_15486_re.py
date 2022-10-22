import sys
input = sys.stdin.readline


N = int(input())

consultants = [[0, 0] for _ in range(N)]

for i in range(N):
    T, P = map(int, input().split())
    consultants[i][0] = T
    consultants[i][1] = P

dp = [0] * (N + 1)

max_value = 0

for day in range(N):
    max_value = max(max_value, dp[day])

    if day + consultants[day][0] > N:
        continue

    dp[day + consultants[day][0]] = max(dp[day + consultants[day][0]], max_value + consultants[day][1])

print(max(dp))