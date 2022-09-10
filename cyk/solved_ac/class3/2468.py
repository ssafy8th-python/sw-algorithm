# 안전 영역
from copy import deepcopy
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0
minV = min(map(min, arr))
maxV = max(map(max, arr))
def bfs(row, col, level, n, temp_arr):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((row, col))
    while q:
        srow, scol = q.pop(0)
        for drow, dcol in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nrow, ncol = srow+drow, scol+dcol
            if 0 <= nrow < n and 0 <= ncol < n and temp_arr[nrow][ncol] > level and visited[nrow][ncol] == 0:
                visited[nrow][ncol] += 1
                temp_arr[nrow][ncol] = 0
                q.append((nrow, ncol))


for level in range(0, maxV+1):
    cnt = 0
    temp_arr = deepcopy(arr)
    for i in range(n):
        for j in range(n):
            if temp_arr[i][j] > level:
                bfs(i,j,level, n, temp_arr)
                cnt += 1
    if res < cnt:
        res = cnt

print(res)