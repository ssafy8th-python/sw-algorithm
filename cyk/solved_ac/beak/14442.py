# 벽 부수고 이동하기2
from collections import deque
import sys
input = sys.stdin.readline
def bfs(r, c):
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
    q = deque([(r,c,0)])
    visited[r][c][0] = 1
    while q:
        cr, cc, colls = q.popleft()
        # if cr == N-1 and cc == M-1:
        #     return visited[cr][cc][colls]
        for dr, dc in dir:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M:
                if colls < K and arr[nr][nc] and not visited[nr][nc][colls+1]:
                    visited[nr][nc][colls+1] = visited[cr][cc][colls] + 1
                    q.append((nr, nc, colls+1))
                elif not arr[nr][nc] and not visited[nr][nc][colls]:
                    visited[nr][nc][colls] = visited[cr][cc][colls] + 1
                    q.append((nr, nc, colls))

    for lst in visited:
        print(lst)

    # 6 4 2
    # 0100
    # 1110
    # 1000
    # 0000
    # 0111
    # 0000
    # [[1, 3, 5], [0, 2, 4], [0, 3, 5], [0, 4, 6]]
    # [[0, 2, 4], [0, 0, 3], [0, 0, 4], [0, 5, 5]]
    # [[0, 0, 3], [0, 8, 4], [0, 7, 5], [0, 6, 6]]
    # [[0, 10, 4], [0, 9, 5], [0, 8, 6], [0, 7, 7]]
    # [[0, 11, 5], [0, 0, 10], [0, 0, 9], [0, 0, 8]]
    # [[0, 12, 6], [0, 13, 7], [0, 14, 8], [0, 15, 9]]

    return -1
N, M, K = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]
dir = [[0,1],[0,-1],[1,0],[-1,0]]
print(bfs(0,0))
