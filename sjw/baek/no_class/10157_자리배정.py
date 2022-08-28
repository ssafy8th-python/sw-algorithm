# 10157 자리배정
# 주소: https://www.acmicpc.net/problem/10157

# 제출한 답
# import sys
# input = sys.stdin.readline

x, y = map(int, input().split())
target = int(input())
visited = [[True] * x for _ in range(y)]

     # 상 우 하 좌
dt = [(-1, 0, 0, 1), (0, 1, 1, 0), (1, 0, 0, -1), (0, -1, -1, 0)]

cnt = 1
idx = 0
r, c = y - 1, 0
visited[r][c] = False
result = [1, 1]
while cnt < x * y and cnt != target:
    nr = r + dt[idx][0]
    nc = c + dt[idx][1]
    if 0 <= nr < y and 0 <= nc < x and visited[nr][nc]:
        cnt += 1
        visited[nr][nc] = False
        r, c = nr, nc
        result = [result[0] + dt[idx][2], result[1] + dt[idx][3]]
    else:
        idx = (idx + 1) % 4

if cnt < target:
    print(0)
else:
    print(*result)
