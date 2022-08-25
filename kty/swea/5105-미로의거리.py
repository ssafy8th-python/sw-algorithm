import sys

sys.stdin = open("input_5105.txt", "r")

def bfs(sti, stj):
    q = []
    visited = [[0] * n for _ in range(n)]
    q.append((sti, stj))
    visited[sti][stj] = 1
    while q:
        i, j = q.pop(0)
        if miro[i][j] == 3:
            return visited[i][j] - 2
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n and miro[ni][nj] != 1 and not visited[ni][nj]:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    miro = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if miro[i][j] == 2:
                sti, stj = i, j

    print(f'#{tc} {bfs(sti, stj)}')