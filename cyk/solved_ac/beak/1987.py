import sys
input = sys.stdin.readline
# def dfs(r, c, cnt):
#     global mx
#     if mx < cnt:
#         mx = cnt
#     for dR, dC in [[0,1],[0,-1],[1,0],[-1,0]]:
#         newR, newC = r+dR, c+dC
#         if 0 <= newR < R and 0 <= newC < C and visited[ord(arr[newR][newC])-65] == 0:
#             visited[ord(arr[newR][newC])-65] = 1
#             dfs(newR, newC, cnt+1)
#             visited[ord(arr[newR][newC])-65] = 0
#
def bfs(r,c):
    global mx
    q = set([(r, c, arr[r][c])])
    while q:
        curR, curC, alp = q.pop()
        for dR, dC in [[0,1],[0,-1],[1,0],[-1,0]]:
            nR, nC = curR+dR, curC+dC
            if 0 <= nR < R and 0 <= nC < C and not arr[nR][nC] in alp:
                q.add((nR, nC, alp+arr[nR][nC]))
                mx = max(mx, len(alp)+1)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
mx = 1
bfs(0,0)
print(mx)

# visited = [0]*26
# visited[ord(arr[0][0])-65] = 1
# dfs(0, 0, 1)


