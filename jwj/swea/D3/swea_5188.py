T = int(input())

INF = 1500


def dynamic():

    for row in range(N):
        for col in range(N):
            n_r, n_c = row, col - 1

            if 0 <= n_r < N and 0 <= n_c < N:
                dp[row][col] = min(dp[row][col], dp[n_r][n_c] + arr[row][col])

            n_r, n_c = row - 1, col
            if 0 <= n_r < N and 0 <= n_c < N:
                dp[row][col] = min(dp[row][col], dp[n_r][n_c] + arr[row][col])


for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    dp = [[INF] * N for _ in range(N)]

    dp[0][0] = arr[0][0]

    dynamic()

    print(f'#{test_case} {dp[N-1][N-1]}')