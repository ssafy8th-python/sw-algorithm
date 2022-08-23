T = int(input())


def dfs(x, y):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        x, y = stack.pop()

        for i in range(4):
            tmp_x = x + deltaX[i]
            tmp_y = y + deltaY[i]

            if 0 <= tmp_x < N and 0 <= tmp_y < N and miro[tmp_x][tmp_y] != '1' and not visited[tmp_x][tmp_y]:
                visited[tmp_x][tmp_y] = True
                stack.append((tmp_x, tmp_y))
                if miro[tmp_x][tmp_y] == '3':
                    return 1

    return 0


for tc in range(1, T+1):
    N = int(input())
    miro = [list(input()) for _ in range(N)]

    deltaX = [-1, 0, 1, 0]
    deltaY = [0, 1, 0, -1]
    visited = [[False] * N for _ in range(N)]

    for idx in range(N):
        if '2' in miro[idx]:
            x, y = idx, miro[idx].index('2')
            break

    visited[x][y] = True

    res = dfs(x, y)

    print(f'#{tc} {res}')
