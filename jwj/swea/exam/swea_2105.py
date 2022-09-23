T = int(input())

delta = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


def dfs(row, col, position, cnt):
    global maxV

    if position == 4:
        if row - 1 == i and col + 1 == j:
            if maxV < cnt:
                maxV = cnt
    else:
        n_x, n_y = row + delta[position][0], col + delta[position][1]
        if 0 <= n_x < N and 0 <= n_y < N and not used[deserts[n_x][n_y]]:
            used[deserts[n_x][n_y]] = True
            dfs(n_x, n_y, position, cnt + 1)
            dfs(n_x, n_y, position + 1, cnt + 1)
            used[deserts[n_x][n_y]] = False
        else:
            dfs(row, col, position+1, cnt)


for test_case in range(1, T+1):
    N = int(input())

    deserts = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * 101

    maxV = 0

    for i in range(N-1):
        for j in range(1, N-1):
            used[deserts[i][j]] = True
            dfs(i, j, 0, 1)
            used[deserts[i][j]] = False

    if maxV == 0:
        maxV = -1

    print(f'#{test_case} {maxV}')