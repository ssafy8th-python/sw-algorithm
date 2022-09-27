# 스도쿠
import sys
input = sys.stdin.readline


arr = [list(map(int, input().split())) for _ in range(9)]

def check1(row, col, value):
    for i in range(9):
        if value == arr[row][i]:
            return False
    return True

def check2(row, col, value):
    for i in range(9):
        if value == arr[i][col]:
           return False
    return True

def check3(row, col, value):

    for i in range(row // 3 * 3, row // 3 * 3 + 3):
        for j in range(col // 3 * 3, col // 3 * 3 + 3):
            if value == arr[i][j]:
                return False

    return True

def dfs(k):
    if k == n:
        for lst in arr:
            print(*lst)
        exit(0)

    curR, curC = zero[k]

    for i in range(1,10):
        if check1(curR, curC, i) and check2(curR, curC, i) and check3(curR, curC, i):
            arr[curR][curC] = i
            dfs(k+1)
            arr[curR][curC] = 0

zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append((i,j))
n = len(zero)
dfs(0)



