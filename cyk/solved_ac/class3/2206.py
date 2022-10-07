# 벽 부수고 이동하기
# 최단 경로
from collections import deque
import sys
input = sys.stdin.readline

dir = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(r, c):
    q = deque([(r,c)])
    visited = [[0]*M for _ in range(N)]
    visited[r][c] = 1
    while q:
        cr, cc = q.popleft()
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not arr[nr][nc]:
                visited[nr][nc] = visited[cr][cc] + 1
                q.append((nr, nc))
    return visited[N-1][M-1]

N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
res = []

for i in range(N):
    for j in range(M):
        for dr, dc in dir:
            nr, nc, nr2, nc2 = dr+i, dc+j, i+dr*2, j+dc*2

        if arr[i][j] == 1:
            arr[i][j] = 0
            res.append(bfs(0,0))
            arr[i][j] = 1

minV = 100000
if not sum(res):
    print(-1)
else:
    for elem in res:
        if elem !=0 and elem < minV:
            minV = elem
    print(minV)