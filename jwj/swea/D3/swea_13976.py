T = int(input())

for tc in range(1, T+1):
    N = int(input())+1

    telecom = [list(input()) for _ in range(N)]

    tower = ['A', 'B', 'C']

    for i in range(N):
        for j in range(N-1):
            for idx, t in enumerate(tower):
                if telecom[i][j] == t:
                    for delta_x, delta_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        n_x, n_y = i + delta_x, j + delta_y
                        for _ in range(0, idx+1):
                            if 0 <= n_x < N and 0 <= n_y < N-1 and telecom[n_x][n_y] == 'H':
                                telecom[n_x][n_y] = 'X'

                            n_x += delta_x
                            n_y += delta_y

    result = 0
    for i in range(N):
        for j in range(N-1):
            if telecom[i][j] == 'H':
                result += 1

    print(f'#{tc} {result}')
