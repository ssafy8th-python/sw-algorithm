# 10966 물놀이 가자
# 주소: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXWXMZta-PsDFAST
import sys
sys.stdin = open("input.txt", "r")
from collections import deque


def bfs():
    q = deque()
    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0
    dt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        r, c = q.popleft()
        for i, j in dt:
            nr = r + i
            nc = c + j
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    result = 0
    for i in visited:
        result += sum(i)

    return result


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ground = [list(input()) for _ in range(n)]

    print(f'#{test_case}', bfs())


from collections import deque


def bfs():
    q = deque()
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if ground[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0
    dt = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        r, c = q.popleft()
        for i in dt:
            nr = r + i[0]
            nc = c + i[1]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and ground[nr][nc] != 'W':
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
    result = 0
    for i in visited:
        result += sum(i)

    return result


T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ground = [list(input()) for _ in range(n)]

    print(f'#{test_case}', bfs())
