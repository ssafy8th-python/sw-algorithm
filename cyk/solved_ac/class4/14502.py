# 연구소
# 0: 빈 칸, 1: 벽, 2: 바이러스
# 안전영역 : 바이러스가 퍼질 수 없는 곳
# 벽을 반드시 3개 세운 후 얻을 수 있는 안전 영역의 크기의 최댓값
import copy
import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def bfs(r,c):
    q = deque([(r,c)])
    visited = [[False]*M for _ in range(N)]
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()
        for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
            nr, nc = cr+dr, cc+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and not arr[nr][nc]:
                arr[nr][nc] = 2
                visited[nr][nc] = False
                q.append((nr,nc))

def comb(v, s):
    global arr, mx
    if v == 3:
        for elem in res:
            arr[zero_list[elem][0]][zero_list[elem][1]] = 1
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    bfs(i, j)

        count_zero = 0
        for lst in arr:
            count_zero += lst.count(0)
        if mx < count_zero:
            mx = count_zero
        arr = copy.deepcopy(original)
        return
    for i in range(s, len(zero_list)-(3-v)+1):
        res[v] = i
        comb(v+1, i+1)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
original = copy.deepcopy(arr)
zero_list = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            zero_list.append((i,j))

res = [-1]*3
mx = 0

comb(0,0)
print(mx)