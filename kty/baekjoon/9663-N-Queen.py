def n_queens(i):
    global cnt
    if i == n:
        cnt += 1
        return

    else:
        for j in range(n):
            col[i] = j
            if promising(i):
                n_queens(i+1)

def promising(i):
    for j in range(i):
        if col[i] == col[j] or abs(col[i]-col[j]) == (i - j):
            return False
    return True

n = int(input())
col = [0] * n
cnt = 0
n_queens(0)
print(cnt)