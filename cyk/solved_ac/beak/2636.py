# 치즈
# 모두 녹기 한 시간 전에 남아있는 치즈조각이 놓여 있는 칸의 개수
# 1은 치즈 0->2는 공기 0은 구멍
from collections import deque
import sys
input = sys.stdin.readline

def bfs1(r, c):     # 치즈 속 구멍 판별
    visited = [[True]*M for _ in range(N)]
    q = deque([(r, c)])
    visited[r][c] = False
    arr[r][c] = 2
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr, nc = cr + dr, cc + dc
            if 0<=nr<N and 0<=nc<M and visited[nr][nc] and (arr[nr][nc] == 2 or not arr[nr][nc]):
                visited[nr][nc] = False
                arr[nr][nc] = 2
                q.append((nr,nc))


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cheeze = 0
for lst in arr:
    cheeze += lst.count(1)
cnt = 0

while True:
    bfs1(0,0)
    melt = deque([])
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                for ar, ac in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if arr[i+ar][j+ac] == 2:
                        melt.append((i, j))
                        break
    for mr, mc in melt:
        arr[mr][mc] = 2

    for lst in arr:
        count += lst.count(1)
    if not count:
        print(cnt+1)
        print(cheeze)
        break
    cheeze = count
    cnt += 1

