# 미로의 거리
'''
3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000
'''

T = int(input())
def find_goal(maze, n):
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                return (i, j)

def bfs(srow, scol, n):
    visited = [[0]*n for _ in range(n)]
    q = []
    q.append((srow, scol))
    visited[srow][scol] = 1
    while q:
        srow, scol = q.pop(0)

        for drow, dcol in [[0,1],[1,0],[0,-1],[-1,0]]:
            nrow, ncol = drow+srow, dcol+scol
            if 0 <= nrow < n and 0 <= ncol < n and maze[nrow][ncol] != 1 and visited[nrow][ncol] == 0:
                q.append((nrow, ncol))
                visited[nrow][ncol] = visited[srow][scol] + 1
                if maze[nrow][ncol] == 3:
                    return visited[nrow][ncol] - 2
    return 0
for tc in range(1, 1+T):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    srow, scol = find_goal(maze, n)
    print(f'#{tc} {bfs(srow, scol, n)}')