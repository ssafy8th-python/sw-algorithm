# 벽 부수고 이동하기
# 최단 경로
from collections import deque
import sys
input = sys.stdin.readline

dir = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs(r, c):
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)] # 방문 여부 + 벽 파괴 확인 => 3차원 배열
    visited[r][c][0] = 1
    q = deque([(r,c,0)])
    while q:
        cr, cc, colls = q.popleft()
        # if cr == N-1 and cc == M-1:
        #     return visited[cr][cc][colls]

        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M:
                if colls == 0 and arr[nr][nc]:  # 벽이고 파괴기회가 0이라면
                    visited[nr][nc][1] = visited[cr][cc][0] + 1
                    q.append((nr, nc, 1))
                elif not visited[nr][nc][colls] and not arr[nr][nc]:  # 이동 가능하면
                    visited[nr][nc][colls] = visited[cr][cc][colls] + 1
                    q.append((nr, nc, colls))

    for lst in visited:
        print(lst)
    # return -1
N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
res = []

print(bfs(0,0))
#
# 6 4
# 0000
# 1110
# 1000
# 0000
# 0111
# 0010

# [[1, 3], [2, 4], [3, 5], [4, 6]]
# [[0, 2], [0, 9], [0, 8], [5, 5]]
# [[0, 11], [8, 4], [7, 5], [6, 6]]
# [[10, 6], [9, 5], [8, 6], [7, 7]]
# [[11, 7], [0, 14], [0, 9], [0, 8]]
# [[12, 8], [13, 9], [0, 14], [0, 9]]
