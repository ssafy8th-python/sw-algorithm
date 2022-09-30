# 보급로
# 파여진 깊이에 비례하여 복구 시간은 증가한다
# 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간 구하기
# S : (0,0), G : (N-1, N-1)
import sys
sys.stdin = open("input (14).txt","r")
from collections import deque

def bfs(r, c):
    q = deque([(r,c)])
    visited = [[10000]*N for _ in range(N)]
    visited[r][c] = 0
    while q:
        curR, curC = q.popleft()
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            nr, nc = curR+dr, curC+dc
            if 0 <= nr < N and 0 <= nc < N:
                tmp = visited[curR][curC] + arr[nr][nc]
                if visited[nr][nc] > tmp:
                    visited[nr][nc] = tmp
                    q.append((nr, nc))

    return visited[N-1][N-1]


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    print(f'#{tc} {bfs(0,0)}')