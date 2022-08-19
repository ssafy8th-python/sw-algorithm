# 숫자배열 회전

import sys
sys.stdin = open("input (4).txt", "r")

T = int(input())

def rotate_1(arr, N):                   # 90도 회전
    rest = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rest[j][N-1-i] = arr[i][j]
    result = []
    for lst in rest:
        result.append(''.join(lst))
    return result

def rotate_2(arr, N):                   # 180도 회전
    rest = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rest[N-1-i][N-1-j] = arr[i][j]
    result = []
    for lst in rest:
        result.append(''.join(lst))
    return result

def rotate_3(arr, N):                   # 270도 회전
    rest = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            rest[N-1-j][i] = arr[i][j]
    result = []
    for lst in rest:
        result.append(''.join(lst))
    return result



for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    # 90도 180도 270도 회전
    res = [[0]*N for _ in range(N)]

    result = [rotate_1(arr, N), rotate_2(arr, N), rotate_3(arr, N)]
    print(f'#{tc}')
    for i in range(N):
        for j in range(3):
            print(result[j][i], end=' ')
        print()