from collections import deque

T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]
    dist = [[-1] * N for _ in range(N)]

    dist[0][0] = 0
    q = deque()
    q.append((0, 0))

    while q:
        row, col = q.popleft()

        if row == N - 1 and col == N - 1:
            continue

        for d_r, d_c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_r, n_c = row + d_r, col + d_c

            if 0 <= n_r < N and 0 <= n_c < N:
                n_value = dist[row][col] + arr[n_r][n_c]
                if dist[n_r][n_c] == -1:
                    dist[n_r][n_c] = n_value
                    q.append((n_r, n_c))
                else:
                    if dist[n_r][n_c] > n_value:
                        dist[n_r][n_c] = n_value
                        q.append((n_r, n_c))

    print(f'#{test_case} {dist[-1][-1]}')