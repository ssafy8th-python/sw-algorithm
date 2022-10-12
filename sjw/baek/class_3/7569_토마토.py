# 7569 토마토
# 주소: https://www.acmicpc.net/problem/7569

# 제출한 답
import sys
input = sys.stdin.readline
from collections import deque


def bfs(arr):
    q = arr
    day = 0
    while q:
        h, r, c = q.popleft()
        for dh, dr, dc in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M:
                if visited[nh][nr][nc] == -1 and not box[nh][nr][nc]:
                    q.append((nh, nr, nc))
                    visited[nh][nr][nc] = visited[h][r][c] + 1
                    day = max(day, visited[nh][nr][nc])

    for h in range(H):
        for r in range(N):
            for c in range(M):
                if not box[h][r][c] and visited[h][r][c] == -1:
                    return -1

    return day


M, N, H = map(int, input().split())
box = []
for _ in range(H):
    tmp = [list(map(int, input().split())) for _ in range(N)]
    box.append(tmp)

# (높이, 행, 열)
start = deque()
visited = [[[-1] * M for _ in range(N)] for _ in range(H)]
for h in range(H):
    for r in range(N):
        for c in range(M):
            if box[h][r][c] == 1:
                start.append((h, r, c))
                visited[h][r][c] = 0

print(bfs(start))
