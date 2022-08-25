T = int(input())


def bfs(num, p_x, p_y):
    visited = [[0] * num for _ in range(num)]
    q = [(p_x, p_y)]
    visited[p_x][p_y] = 1

    while q:
        c_x, c_y = q.pop(0)

        if miro[c_x][c_y] == '3':
            return visited[c_x][c_y] - 2
        else:
            for d_i, d_j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                n_x, n_y = c_x+d_i, c_y+d_j

                if 0 <= n_x < num and 0 <= n_y < num and miro[n_x][n_y] != '1' and visited[n_x][n_y] == 0:
                    q.append((n_x, n_y))
                    visited[n_x][n_y] = visited[c_x][c_y] + 1

    return 0


for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    x, y = 0, 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '2':
                x = i
                y = j
                break

        if x != 0:
            break

    print(f'#{tc} {bfs(N, x, y)}')


