# 10966 물놀이 가자
# 주소: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST
import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs(r, c):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    dt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        r, c = q.popleft()
        if ground[r][c] == 'W':
            return visited[r][c] - 1
        for i in dt:
            nr = r + i[0]
            nc = c + i[1]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ground = [list(input()) for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'L':
                result += bfs(i, j)

    print(f'#{test_case}', result)


