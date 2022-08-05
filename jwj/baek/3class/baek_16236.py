import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((position[0], position[1], 0))
    
    while que:
        x, y, cnt = que.popleft()
        if target[0] == x and target[1] == y:
            return cnt

        for i in range(4):
            x_i = x + x_idx[i]
            y_i = y + y_idx[i]
            
            if (0 <= x_i < N) and (0 <= y_i < N) and (sea[x_i][y_i] <= size) and visited[x_i][y_i]:
                visited[x_i][y_i] = 0
                que.append((x_i, y_i, cnt+1))
                visited[x_i][y_i] = 1

N = int(input())

sea = []
position = [0, 0]
x_idx = [-1, 0, 1, 0]
y_idx = [ 0, -1, 0, 1]
size = 2
size_cnt = 0
time = 0
target = [0, 0]
visited = [[1] * N for _ in range(N)]
for i in range(N):
    tmp_lst = list(map(int, input().split()))
    sea.append(tmp_lst)
    for idx, num in enumerate(tmp_lst):
        if num == 9:
            position = [i, idx]
        
while True:
    min_cnt = 2000000
    cnt = 0

    last_target = [-1, -1]

    for i in range(N):
        for j in range(N):
            if sea[i][j] != 0 and sea[i][j] < size:
                target = [i, j]
                cnt = bfs()
                if min_cnt > cnt:
                    last_target = [i, j]
                    min_cnt = cnt

    sea[position[0]][position[1]] = 0
    position = [last_target[0], last_target[1]]
    sea[position[0]][position[1]] = 9

    size_cnt += 1

    if size == size_cnt:
        size += 1
        size_cnt = 0

    if cnt == 0:
        break
    
    time += min_cnt



print(time)


