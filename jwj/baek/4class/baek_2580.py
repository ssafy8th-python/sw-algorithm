def dfs(cur_x, cur_y):

    if cur_y == 9:
        cur_x += 1
        cur_y = 0

    if cur_x == 9:
        for i in garo_sudoku:
            for j in i:
                print(j, end=' ')
            print()
        exit()

    if garo_sudoku[cur_x][cur_y]:
        dfs(cur_x, cur_y+1)
        return

    for i in range(1, 10):

        # 가로 검사
        if i in garo_sudoku[cur_x]:
            continue
        # 세로 검사
        if i in sero_sudoku[cur_y]:
            continue

        # 네모 검사
        if i in nemo_sudoku[cur_x//3][cur_y//3]:
            continue

        garo_sudoku[cur_x][cur_y] = i
        sero_sudoku[cur_y].append(i)
        nemo_sudoku[cur_x//3][cur_y//3].append(i)

        dfs(cur_x, cur_y + 1)

        garo_sudoku[cur_x][cur_y] = 0
        sero_sudoku[cur_y].pop()
        nemo_sudoku[cur_x//3][cur_y//3].pop()


# 가로
garo_sudoku = [list(map(int, input().split())) for _ in range(9)]

# 세로
sero_sudoku = [[] for _ in range(9)]

# 네모
nemo_sudoku = [[[] for _ in range(3)] for _ in range(3)]

idx = 0
for s in zip(*garo_sudoku):
    for n in s:
        if n:
            sero_sudoku[idx].append(n)
    idx += 1

for i in range(9):
    for j in range(9):
        if garo_sudoku[i][j]:
            nemo_sudoku[i // 3][j // 3].append(garo_sudoku[i][j])

dfs(0, 0)