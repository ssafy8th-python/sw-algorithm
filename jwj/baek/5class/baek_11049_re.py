N = int(input())

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

# 검사할 개수
for size in range(1, N):
    for start in range(0, N - size):    # 시작 위치 행
        end = start + size              # 끝 위치

        if size == 1:                   # size가 1이면 하나의 값만 계산하면 됨
            dp[start][end] = matrix[start][0] * matrix[start][1] * matrix[end][1]
            continue

        dp[start][end] = 2 ** 31

        for k in range(start, end):
            dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] +
                                 matrix[start][0] * matrix[k][1] * matrix[end][1])

print(dp[0][-1])
