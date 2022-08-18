dp = [0] * 31

dp[1] = 1
dp[2] = 3

for num in range(3, 31):
    dp[num] = dp[num-1] + 2* (dp[num-2])

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    N //= 10

    print(f'#{tc} {dp[N]}')

