T = int(input())


def dfs(position):

    if miro[position[0]][position[1]] == 3:
        return 1
    else:
        for i in range(4):
            tmp_x = position[0] + deltaX[i]
            tmp_y = position[1] + deltaY[i]

            if 0 <= tmp_x < N and 0 <= tmp_y < N and miro[tmp_x][tmp_y] != 1 and not visited[tmp_x][tmp_y]:
                visited[tmp_x][tmp_y] = True
                res = dfs([tmp_x, tmp_y])

                if res == 1:
                    return 1
    return 0


for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]

    position = []

    deltaX = [-1, 0, 1, 0]
    deltaY = [0, 1, 0, -1]
    visited = [[False] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if miro[x][y] == 2:
                position = [x, y]
                break
        if position:
            break

    visited[position[0]][position[1]] = True

    res = dfs(position)

    print(f'#{tc} {res}')
