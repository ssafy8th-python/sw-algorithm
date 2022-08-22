import sys

sys.stdin = open("input_1961.txt", "r")


def rotation(src):
    ARR = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ARR[i][j] = src[j][N-i-1]
    return ARR

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr_90 = rotation(arr)
    arr_180 = rotation(arr_90)
    arr_270 = rotation(arr_180)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, arr_270[i])),end=' ')
        print(''.join(map(str, arr_180[i])),end=' ')
        print(''.join(map(str, arr_90[i])))