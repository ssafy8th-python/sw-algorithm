# 유기농 배추
t = int(input())
def bfs(srow, scol, N, M):
    q = []
    q.append((srow, scol))
    visited[srow][scol] = 1
    arr[srow][scol] = 0
    while q:
        srow, scol = q.pop(0)
        for drow, dcol in [[1,0], [0,1], [-1,0], [0,-1]]:
            nrow, ncol = srow+drow, scol+dcol
            if 0<= nrow < N and 0<= ncol < M and arr[nrow][ncol] !=0 and visited[nrow][ncol] == 0:
                arr[nrow][ncol] = 0
                q.append((nrow, ncol))
                visited[nrow][ncol] = 1


for tc in range(t):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    for _ in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                bfs(i, j, N, M)
                cnt +=1
    print(cnt)