# 미로
# import sys
# sys.stdin = open("input (2).txt", "r")

def find(maze):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return (i, j)

def dfs(Crow, Ccol, n):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((Crow, Ccol))
    visited[Crow][Ccol] = 1
    while q:
        Crow, Ccol = q.pop(0)
        if maze[Crow][Ccol] == 3:
            return 1
        for dR, dC in [[0,1],[1,0],[0,-1],[-1,0]]:
            nR, nC = Crow + dR, Ccol +dC
            if 0 <= nR < n and 0 <= nC < n and maze[nR][nC] != 1 and visited[nR][nC] == 0:
                q.append((nR, nC))
                visited[nR][nC] = visited[Crow][Ccol] + 1
    return 0

for _ in range(1, 11):
    tc = int(input())
    n = 16
    maze = [list(map(int, input())) for _ in range(n)]
    Crow, Ccol = find(maze)
    print(f'#{tc} {dfs(Crow, Ccol, n)}')