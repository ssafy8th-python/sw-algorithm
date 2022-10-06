from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    dp = [0] * 2000000

    dp[N] = 1

    q = deque()

    q.append(N)

    while q:
        num = q.popleft()

        if num == M:
            break

        n_x = num * 2
        if n_x < 2000000 and not dp[n_x]:
            dp[n_x] = dp[num] + 1
            q.append(n_x)

        n_x = num + 1
        if n_x < 2000000 and not dp[n_x]:
            dp[n_x] = dp[num] + 1
            q.append(n_x)

        n_x = num - 1
        if n_x >= 0 and not dp[n_x]:
            dp[n_x] = dp[num] + 1
            q.append(n_x)

        n_x = num - 10
        if n_x >= 0 and not dp[n_x]:
            dp[n_x] = dp[num] + 1
            q.append(n_x)

    print(f'#{test_case} {dp[M] - 1}')
