# 적록색약
import copy
from collections import deque
from copy import deepcopy
def bfs(r, c, ar):
    q = deque([(r, c)])
    visited = [[0]*n for _ in range(n)]
    visited[r][c] = 1
    letter = ar[r][c]

    while q:
        curR, curC = q.popleft()
        for dR, dC in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nR, nC = curR+dR, curC+dC
            if 0 <= nR < n and 0 <= nC < n and not visited[nR][nC] and ar[nR][nC] == letter:
                q.append((nR, nC))
                visited[nR][nC] = 1
                ar[nR][nC] = 0

n = int(input())
arr = [list(input()) for _ in range(n)]
arr2 = copy.deepcopy(arr)
cnt = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            bfs(i,j, arr)
            cnt += 1

for i in range(n):
    for j in range(n):
        if arr2[i][j] == 'G':
            arr2[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if arr2[i][j]:
            bfs(i, j, arr2)
            cnt2 += 1

print(cnt, cnt2)
