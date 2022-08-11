import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    global can_eat, min_cnt
    visited = [[False] * N for i in range(N)]
    visited[position[0]][position[1]] = True

    d_que = deque()
    d_que.append((position[0], position[1], 0))
    distance = []

    while d_que:
        x, y, cnt = d_que.popleft()

        for idx in t_idx:
            x_next = x + idx[0]
            y_next = y + idx[1]

            if 0 <= x_next < N and 0 <= y_next < N and not visited[x_next][y_next]:
                if sea[x_next][y_next] <= size:
                    visited[x_next][y_next] = True
                    if 0 < sea[x_next][y_next] < size:
                        min_cnt = cnt
                        distance.append((cnt+1, x_next, y_next))

                    if cnt+1 <= min_cnt:
                        d_que.append((x_next, y_next, cnt + 1))

    if distance:
        distance.sort()
        return distance[0]

    else:
        return False

N = int(input())

sea = []
position = []
size = 2
eat = 0
time = 0
fish_cnt = 0
min_cnt = 400


t_idx = [[0, -1], [-1, 0], [0, 1], [1, 0]]

for idx in range(N):
    sea.append(list(map(int, input().split())))
    for j in range(N):
        if 0 < sea[idx][j] <= 6:
            fish_cnt += 1
        if sea[idx][j] == 9:
            position = [idx, j]

sea[position[0]][position[1]] = 0

while fish_cnt:
    min_cnt = 400

    result = bfs()
    if not result:
        break

    time += result[0]
    eat += 1
    fish_cnt -= 1

    position = [result[1], result[2]]
    sea[result[1]][result[2]] = 0

    if size == eat:
        size += 1
        eat = 0


print(time)
