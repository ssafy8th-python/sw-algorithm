# 토마토
# 토마토가 익는 최소일수 구하기
# 저장될 때부터 모든 토마토가 익어있는 상태이면 0 출력, 토마토가 익지 못하는 상황이면 -1 출력
from collections import deque
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def bfs(lst):
    visited = [[0]*M for _ in range(N)]
    q = deque([])
    for elem in lst:
        q.append(elem)
    cnt = 0
    while q:
        cR, cC = q.popleft()
        visited[cR][cC] == 1

        for dR, dC in [[1,0], [-1,0], [0,1], [0,-1]]:
            nR, nC = cR + dR, cC + dC
            if 0 <= nR < N and 0 <= nC < M and visited[nR][nC] == 0 and arr[nR][nC] == 0:
                visited[nR][nC] = visited[cR][cC] + 1
                arr[nR][nC] = 1
                q.append((nR, nC))

    return max(map(max, visited))
lst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            lst.append((i,j))

res = bfs(lst)
for lst in arr:
    if 0 in lst:
        print(-1)
        break
else:
    print(res)
