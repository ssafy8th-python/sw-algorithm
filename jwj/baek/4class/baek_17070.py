import sys
input = sys.stdin.readline

def is_check(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False


def dfs(x, y, d):
    global cnt

    if x == N - 1 and y == N - 1:
        cnt += 1
        return
    
    if d == 0:
        n_x, n_y = x, y + 1
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0':
            dfs(n_x, n_y, 0)


        n_x, n_y = x + 1, y + 1
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0' and arr[n_x][n_y-1] == '0' and arr[n_x-1][n_y] == '0':
            dfs(n_x, n_y, 2)

    elif d == 1:
        n_x, n_y = x + 1 , y
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0':
            dfs(n_x, n_y, 1)


        n_x, n_y = x + 1, y + 1
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0' and arr[n_x][n_y-1] == '0' and arr[n_x-1][n_y] == '0':
            dfs(n_x, n_y, 2)
    else:
        n_x, n_y = x, y + 1
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0':
            dfs(n_x, n_y, 0)

        n_x, n_y = x + 1, y
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0':
            dfs(n_x, n_y, 1)


        n_x, n_y = x + 1, y + 1
        if is_check(n_x, n_y) and arr[n_x][n_y] == '0' and arr[n_x][n_y-1] == '0' and arr[n_x-1][n_y] == '0':
            dfs(n_x, n_y, 2)




N = int(input())

arr = [input().split() for _ in range(N)]

cnt = 0

# 끝 점, 가로:0, 세로:1, 대각선:2
dfs(0, 1, 0)

print(cnt)