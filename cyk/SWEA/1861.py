# 정사각형 방
import sys
sys.stdin = open("input (10).txt", "r")
'''
2
2
1 2
3 4
3
9 3 4
6 1 5
7 8 2
'''
T = int(input())
def check(row, col):
    q = [(row, col)]
    visited[row][col] = 1
    resR, resC = 0,0
    tmp = 100000000
    cnt = 0
    result = 0
    while q:

        Crow, Ccol = q.pop(0)
        if tmp > arr[Crow][Ccol]:
            tmp = arr[Crow][Ccol]

        for drow, dcol in [[-1,0], [1,0], [0,-1], [0,1]]:
            nrow, ncol = Crow+drow,  Ccol+dcol
            if 0 <= nrow < n and 0 <= ncol < n and visited[nrow][ncol] == 0 and abs(arr[nrow][ncol] - arr[Crow][Ccol]) == 1:
                cnt += 1
                q.append((nrow, ncol))
                visited[nrow][ncol] = 1

    return (cnt, tmp)

for tc in range(1, 1+T):
    res = 0
    idx = {}
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for row in range(0, n):
        for col in range(0, n):
            val = check(row, col)
            if res <= val[0]:
                res = val[0]
                if res in idx.keys():
                    idx[res].append(val[1])
                else:
                    idx[res] = [val[1]]
    print(f'#{tc} {min(idx[max(idx.keys())])} {res+1}')