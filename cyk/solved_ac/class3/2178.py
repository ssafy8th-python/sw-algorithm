# 미로 탐색
# (1,1)에서 출발하여 (N,M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램
'''
4 6
101111
101010
101011
111011
'''
def bfs(srow, scol, N, M):
    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((srow, scol))
    visited[srow][scol] = 1
    while q:
        srow, scol = q.pop(0)
        for drow, dcol in [[0,1],[1,0],[0,-1],[-1,0]]:
            nrow, ncol = drow+srow, dcol+scol
            if 0 <= nrow < N and 0 <= ncol <M and maze[nrow][ncol] != 0 and visited[nrow][ncol] == 0:
                q.append((nrow, ncol))
                visited[nrow][ncol] = visited[srow][scol] + 1
                if nrow == N-1 and ncol == M-1:
                    return visited[nrow][ncol]
    return 0
N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
srow, scol = 0, 0                        # 출발 (1,1)=>(0,0)
print(bfs(srow, scol, N, M))
