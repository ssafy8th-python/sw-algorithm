# 최소 비용
# import sys
# sys.stdin = open("sample_input (4).txt", "r")

from collections import deque

def bfs(r, c):
    visited = [[10000000]*n for _ in range(n)]
    q = deque([(r,c)])
    visited[r][c] = 0
    while q:
        curR, curC = q.popleft()
        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            newR, newC = curR+dr, curC+dc

            if 0 <= newR < n and 0 <= newC < n:
                tmp = visited[curR][curC] + 1
                if arr[curR][curC] < arr[newR][newC]:
                    abs_value = arr[newR][newC] - arr[curR][curC]
                    if visited[newR][newC] > tmp + abs_value:
                        visited[newR][newC] = tmp + abs_value
                        q.append((newR, newC))
                else:
                    if visited[newR][newC] > tmp :
                        visited[newR][newC] = tmp
                        q.append((newR, newC))

    return visited[n-1][n-1]

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(f'#{tc} {bfs(0,0)}')

