import sys

sys.stdin = open("input_gizi.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(input()) for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A':
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'H':
                        arr[ni][nj] = 'X'

            elif arr[i][j] == 'B':
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    for k in range(1, 3):
                        ni = i + di * k
                        nj = j + dj * k
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'

            elif arr[i][j] == 'C':
                for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    for k in range(1, 4):
                        ni = i + di * k
                        nj = j + dj * k
                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 'H':
                            arr[ni][nj] = 'X'
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt += 1

    print(f'#{tc} {cnt}')
