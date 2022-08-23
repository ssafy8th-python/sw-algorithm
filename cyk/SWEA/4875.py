# 미로
def check(s_row, s_col):
    dR = [-1, 1, 0, 0]
    dC = [0, 0, -1, 1]

    if arr[s_row][s_col] == 3:
            return s_row, s_col
    else:
        for d in range(4):
            new_row, new_col = s_row + dR[d], s_col + dC[d]
            if 0 <= new_row < n and 0 <= new_col < n and arr[new_row][new_col] != 1 and check_arr[new_row][new_col] == True:
                check_arr[new_row][new_col] = False
                res = check(new_row, new_col)
                if res != None:
                    return res

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, list(input()))) for _ in range(n)]

    s_row, s_col = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                s_row, s_col = i, j
                break
    check_arr = [[True]*n for _ in range(n)]
    print(f'#{tc} ', end='')
    if check(s_row, s_col) == None:
        print(0)
    else:
        print(1)