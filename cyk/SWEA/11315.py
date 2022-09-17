# 오목판정
# def divid(arr):
#     pass
# N = int(input())
# arr = [[0]*2**N for _ in range(2**N)]
# print(arr)

# def check(row, col):
#     for d in range(4):
#         while 적 방향의 값이 'o'인 동안:
#             cnt += 1
#         if cnt >= 5:
#             return True
#     return False

# for row in range():
#     for col in range():
#         if arr[row][col == 'o':
#             check(row, col)

import sys
sys.stdin = open("sample_input.txt", "r")



def checking(arr, n):
    for lst in arr:
        check = 0
        for i in range(n):
            if lst[i] == 'o':
                check += 1
            else:
                check = 0
            if check == 5:
                return 'YES'                

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    Hor_check = checking(arr, n)                
    
    vert = list(zip(*arr))
    Ver_check = checking(vert, n)
    
    check = 0
    check2 = 0
    Cross_check = ''
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i+j < n and k+j <n and arr[i+j][j+k] == 'o':
                    check += 1
                else:
                    check = 0
                if check == 5:
                    Cross_check = 'YES'
                    break
                
                if i+j < n and n-j-1-k >= 0 and arr[i+j][n-j-1-k] == 'o':
                    check2 += 1
                else:
                    check2 = 0
                if check2 == 5:
                    Cross_check = 'YES'
                    break
        

    print(f'#{tc}', end=' ')
    if Hor_check or Ver_check or Cross_check:
        print('YES')
    else:
        print('NO')