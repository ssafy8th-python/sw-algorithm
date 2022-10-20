# 로봇청소기
# 1. 현재 위치 청소
# 2. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례로 탐색
#     2-1. 회전한 다음 한칸 전진
#     2-2. 청소할 공간이 없다면 회전
#     2-3. 네 방향 모두 청소가 되어있거나 벽인 경우 방향 유지한채로 한 칸 후진
#     2-4. 뒤쪽도 벽이라면 작동 정지
from collections import deque
import sys
iput = sys.stdin.readline
# 0: 북, 1: 동, 2: 남, 3: 서
dir = [[-1,0],[0,1],[1,0],[0,-1]]
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

while True:
    arr[r][c] = 2   # 현재 방향 청소

    nd = (d+3)%4    # 현재 방향의 왼쪽 방향
    nr, nc = r+dir[nd][0], c+dir[nd][1] # 왼쪽 방향 전진

    if arr[nr][nc] == 0:
        d = nd
        r, c = nr, nc
    else:   # 왼쪽 방향이 청소되어있거나 벽이라면
        tmp = []
        back = (d+2)%4
        for dr, dc in dir:
            tmp.append(arr[r+dr][c+dc])
        if 0 not in tmp and arr[r+dir[back][0]][c+dir[back][1]] == 1:
            break
        elif 0 not in tmp and arr[r+dir[back][0]][c+dir[back][1]] != 1:
            r, c = r+dir[back][0], c+dir[back][1]
        else:
            d = nd
res = 0
for i in arr:
    res += i.count(2)
    print(*i)
print(res)


