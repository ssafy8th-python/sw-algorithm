from copy import deepcopy


def dfs(num, lst, s, v):
    global minV
    global g_core
    global tmp_minV

    if v > g_core:
        g_core = v
        tmp_minV = s

    if v == g_core:
        if tmp_minV > s:
            tmp_minV = s

    if num == core_num:
        if minV > s and v == core_num:
            minV = s
        return

    else:
        check = 0
        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            cnt = 0
            x = core_lst[num][0]
            y = core_lst[num][1]
            n_x = x + d_x
            n_y = y + d_y

            while 0 <= n_x < N and 0 <= n_y < N:
                if lst[n_x][n_y] > 0:
                    break
                cnt += 1
                n_x += d_x
                n_y += d_y
            else:
                check = 1
                tmp_lst = deepcopy(lst)

                for _ in range(cnt):
                    n_x -= d_x
                    n_y -= d_y
                    tmp_lst[n_x][n_y] = 2
                dfs(num+1, tmp_lst, s+cnt, v+1)

        if not check:
            dfs(num+1, lst, s, v)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    maps = [list(map(int, input().split())) for _ in range(N)]

    core_num = 0

    core_lst = []

    minV = 1000000

    g_core = 0

    tmp_minV = 1000000

    for i in range(N):
        for j in range(N):
            if maps[i][j]:
                core_lst.append((i, j))
                core_num += 1

    n = 0
    for idx, position in enumerate(core_lst):
        for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_x = position[0] + d_x
            n_y = position[1] + d_y

            if 0 > n_x and N <= n_x and  0 > n_y and N <= n_y:
                core_num -= 1
                core_lst.pop(idx)
                break

    dfs(0, maps, 0, 0)

    if g_core != core_num:
        minV = tmp_minV

    print(f'#{tc} {minV}')
