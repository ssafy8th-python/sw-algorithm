# 다리 만들기
from collections import deque
import sys

input = sys.stdin.readline
def bfs1(r, c, color):      # 섬 구분
    q = deque([(r, c)])
    visited = [[True]*N for _ in range(N)]
    visited[r][c] = False
    arr[r][c] = color
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] and arr[nr][nc] == 1:
                arr[nr][nc] = color
                visited[nr][nc] = False
                q.append((nr, nc))

def bfs2(v):
    global res
    visited = [[-1]*N for _ in range(N)]
    q = deque()

    for i in range(N):
        for j in range(N):
            if arr[i][j] == v:      # v번 섬의 좌표
                q.append((i, j))
                visited[i][j] = 0

    while q:
        cr, cc = q.popleft()
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > 0 and arr[nr][nc] != v:    # 다른 섬에 간 경우
                    res = min(res, visited[cr][cc])
                    return
                if arr[nr][nc] == 0 and visited[nr][nc] == -1:  # 바다인 경우
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
color = 1
res = sys.maxsize
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            bfs1(i, j, color)
            color += 1

for lst in arr:
    print(lst)

for i in range(1, color):   # 각각의 섬들 출발
    bfs2(i)

print(res)