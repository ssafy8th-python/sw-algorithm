# 토마토
# 토마토가 익을 때까지 걸리는 최소일수 계산
# 가장 밑의 상자부터 가장 위의 상자까지 저장된 토마토들의 정보

from collections import deque
import sys
input = sys.stdin.readline

def bfs(rLst):
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(B)]
    q = deque([])
    for elem in rLst:
        q.append(elem)

    while q:
        cl, cr, cc = q.popleft()
        if visited[cl][cr][cc] == 0:
            visited[cl][cr][cc] = 1
        for dl, dr, dc in [[0,-1,0],[0,1,0],[0,0,-1],[0,0,1],[-1,0,0],[1,0,0]]:  # 위, 아래, 왼쪽, 오른쪽,앞, 뒤
            nl, nr, nc = cl+dl, cr+dr, cc+dc
            if 0 <= nl < B and 0 <= nr < N and 0 <= nc < M and thArr[nl][nr][nc]==0 and visited[nl][nr][nc]==0:
                visited[nl][nr][nc] = visited[cl][cr][cc] + 1
                thArr[nl][nr][nc] = 1
                q.append((nl, nr, nc))
    res = 0
    for arr in visited:
        if res < max(map(max, arr)):
            res = max(map(max, arr))


    return res -1

M, N, B = map(int, input().split()) # 상자의 가로, 세로, 개수

# 3차원 배열
thArr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(B)]

rLst = []

for k in range(B):
    for i in range(N):
        for j in range(M):
            if thArr[k][i][j] == 1:
                rLst.append((k, i, j))

result = bfs(rLst)
for arr in thArr:
    for lst in arr:
        if 0 in lst:
            print(-1)
            exit(0)
else:
    print(result)
