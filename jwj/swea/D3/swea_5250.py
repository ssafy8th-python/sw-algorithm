from collections import deque

T = int(input())

INF = int(1e9)

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    fuel_arr = [[INF] * N for _ in range(N)]
    fuel_arr[0][0] = 0
    q = deque()
    q.append((0, 0, arr[0][0]))

    while q:
        row, col, h = q.popleft()

        if row == N-1 and col == N-1:
            continue
        else:
            for d_x, d_y in ((1, 0), (0, 1), (0, -1), (-1, 0)):
                n_x = row + d_x
                n_y = col + d_y

                if 0 <= n_x < N and 0 <= n_y < N:
                    diff_h = arr[row][col] - arr[n_x][n_y]
                    new_fuel = fuel_arr[row][col] + 1

                    if diff_h < 0:
                        new_fuel -= diff_h

                    if fuel_arr[n_x][n_y] > new_fuel:
                        fuel_arr[n_x][n_y] = new_fuel
                        q.append((n_x, n_y, arr[n_x][n_y]))

    print(f'#{test_case} {fuel_arr[-1][-1]}')
