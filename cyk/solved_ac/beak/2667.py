n = int(input())
arr = [list(map(int,list(input()))) for _ in range(n)]

def bfs(row, col, n):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((row, col))
    visited[row][col] = 1
    cnt = 0
    while q:
        curR, curC = q.pop(0)
        for drow, dcol in [[0,1], [0,-1], [1, 0], [-1, 0]]:
            nrow = curR + drow
            ncol = curC + dcol
            if 0<= nrow <n and 0<= ncol <n and arr[nrow][ncol] == 1 and visited[nrow][ncol] == 0:
                arr[nrow][ncol] = 0
                visited[nrow][ncol] = 1
                q.append((nrow, ncol))
                cnt += 1
    return cnt

res = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            res.append(bfs(i, j, n)+1)

print(len(res))
for elem in sorted(res):
    print(elem)
