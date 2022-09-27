import copy

T = int(input())


def resize(arr):
    # H-1 ~ 0
    for row in range(H-1, -1, -1):
        # 0 ~ W
        for col in range(W):
            if arr[row][col] == 0:
                continue

            # 0이 아님 이동
            n_row = row + 1

            while n_row < H:
                if arr[n_row][col] == 0:
                    arr[n_row][col] = arr[n_row-1][col]
                    arr[n_row-1][col] = 0
                else:
                    break
                n_row += 1


def boom(arr, row, col):
    q = [(row, col, arr[row][col])]

    while q:
        r, c, cnt = q.pop()

        arr[r][c] = 0

        for d_r, d_c in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            n_r, n_c = r + d_r, c + d_c
            for _ in range(cnt - 1):
                if n_r < 0 or n_r >= H or n_c < 0 or n_c >= W:
                    break

                q.append((n_r, n_c, arr[n_r][n_c]))
                arr[n_r][n_c] = 0
                n_r += d_r
                n_c += d_c


def find(arr, col):
    row = 0
    while row < H:
        if arr[row][col]:
            return row
        row += 1
    return -1


def drop(depth, arr):
    global minV
    if depth == N:
        result = 0
        for i in range(H):
            for j in range(W):
                if arr[i][j]:
                    result += 1

        if minV > result:
            minV = result
        return

    for col in range(W):
        row = find(arr, col)
        if row == -1:
            continue

        backup = copy.deepcopy(arr)
        boom(backup, row, col)
        resize(backup)
        drop(depth + 1, backup)


for test_case in range(1, T+1):
    N, W, H = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(H)]

    minV = 1000

    drop(0, arr)

    if minV == 1000:
        minV = 0

    print(f'#{test_case} {minV}')