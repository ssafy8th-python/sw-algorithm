import sys

sys.stdin = open("input_2806.txt", "r")

def n_queens(i, col):
    global cnt
    if i == n:
        cnt += 1
        return
    for j in range(n):
        col[i] = j
        if promising(i, col):
            n_queens(i + 1, col)

def promising(i, col):
    for j in range(i):
        if col[i] == col[j] or abs(col[i]-col[j]) == (i - j):
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    col = [0] * n
    cnt = 0
    n_queens(0, col)
    print(f'#{tc} {cnt}')