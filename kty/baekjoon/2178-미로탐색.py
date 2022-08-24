def bfs(i, j):
    q = []
    visited = [[0] * m for _ in range(n)]
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        if i+1 == n and j+1 == m:
            return visited[i][j]
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and maze[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))
