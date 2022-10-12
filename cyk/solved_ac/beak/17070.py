# 파이프 옮기기 1
# 파이프를 밀 수 있는 방향은 오른쪽, 아래, 오른쪽 아래 대각선 방향
# 가로, 세로 : 2가지, 대각선 : 3가지
# 빈칸은 0 벽은 1
import sys
input = sys.stdin.readline

def dfs(sr, sc, r,c):
    global res
    if r == N-1 and c == N-1:
        res += 1
        return

    # 끝점의 이동 경로
    if sr != r and sc == c:           # 세로 방향
        if 0 <= r+1 < N and not arr[r+1][c]:
            dfs(r, c, r+1, c)
        if 0 <= r+1 < N and 0 <= c+1 < N and not arr[r+1][c+1] and not arr[r+1][c] and not arr[r][c+1]:
            dfs(r, c, r+1, c+1)
    elif sc != c and sr == r:         # 가로 방향
        if 0 <= c+1 < N and not arr[r][c+1]:
            dfs(r, c, r, c+1)
        if 0 <= r+1 < N and 0 <= c+1 < N and not arr[r+1][c+1] and not arr[r+1][c] and not arr[r][c+1]:
            dfs(r, c, r+1, c+1)
    else:                   # 대각선 방향
        if 0 <= r+1 < N and not arr[r+1][c]:
            dfs(r, c, r+1, c)
        if 0 <= c + 1 < N and not arr[r][c + 1]:
            dfs(r, c, r, c+1)
        if 0 <= r+1 < N and 0 <= c+1 < N and not arr[r+1][c+1] and not arr[r+1][c] and not arr[r][c+1]:
            dfs(r, c, r+1, c+1)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0

dfs(0,0,0,1)
print(res)









#
#
# def bfs(sr, sc, r,c):
#     global res
#     q = deque([(sr, sc, r,c)])
#     while q:
#         csr, csc, cr, cc = q.popleft()
#         if cr == N-1 and cc == N-1:
#             res += 1
#         # 끝점의 이동 경로
#         if csr != cr and csc == cc:           # 세로 방향
#             dir = [[1,0],[1,1]]
#         elif csc != cc and csr == cr:         # 가로 방향
#             dir = [[0,1],[1,1]]
#         else:                   # 대각선 방향
#             dir = [[0,1],[1,1],[1,0]]
#
#         for dr, dc in dir:
#             nr, nc = cr+dr, cc+dc
#             if 0 <= nr < N and 0 <= nc < N  and not arr[nr][nc]:
#                 if dr==1 and dc == 1:       # 대각선으로 지날때 방해물 없는지 확인
#                     if not arr[cr+1][cc] and not arr[cr][cc+1]:
#                         q.append((cr, cc, nr, nc))
#                 else:
#                     q.append((cr, cc, nr, nc))
