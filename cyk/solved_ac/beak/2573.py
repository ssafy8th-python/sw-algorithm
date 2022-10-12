# 빙산
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간
# 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0 출력
from collections import deque
import sys
input = sys.stdin.readline

def bfs(r,c):
    q = deque([(r,c)])
    # visited[r][c] = False
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
            nr, nc = dr+cr, dc+cc
            if 0 <= nr < N and 0 <= nc <M and arr[nr][nc] and visited[nr][nc]:
                zero_count = 0
                for ar, ac in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    if visited[nr+ar][nc+ac] and arr[nr+ar][nc+ac] == 0:
                        zero_count += 1
                arr[nr][nc] -= zero_count
                if arr[nr][nc] < 0:
                    arr[nr][nc] = 0

                visited[nr][nc] = False
                q.append((nr, nc))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
flag = False
while True:
    visited = [[True]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] and visited[i][j]:
                bfs(i, j)
                cnt += 1
        if cnt > 1:
            flag = True
            break
    if flag:
        print(res)
        break
    sum_arr = 0
    for lst in arr:
        sum_arr += sum(lst)
    if sum_arr == 0:
        print(0)
        break
    res += 1
