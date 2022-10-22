# 16236 아기 상어
# 주소: https://www.acmicpc.net/problem/16236

# 제출한 답

# 1초에 상하좌우 한 칸
# 크기가 같거나 작은 칸만 지나갈 수 있음
# 크기가 작은 물고기만 취식 가능
# 먹을 물고기가 없다면 끝
# 그 위치로 가는데 지나야하는 칸의 개수가 최소인 물고기 먹음
# 가까운 물고기가 많으면 가장 위, 그 중에서 가장 왼쪽 먼저 먹음
# 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기 1증가

# 물고기 상태 전부 저장
# 그 중에 현재 크기보다 작은 물고기와의 거리만 계산
# 크기가 작은 물고기가 없거나 갈 수 있는 곳이 없다면 종료
# 그 장소로 이동 후 위 반복

import sys
input = sys.stdin.readline
from collections import deque


def bfs(shark, lg):
    visited = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((shark[0], shark[1]))
    visited[shark[0]][shark[1]] = 0
    results = []
    while q and lg:
        r, c = q.popleft()
        if (r, c) in goal and board[r][c]:
            results.append((r, c, visited[r][c]))
            lg -= 1
        else:
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] <= size and visited[nr][nc] == -1:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
    if results:
        results.sort(key=lambda x: (x[2], x[0], x[1]))
        return results[0]
    else:
        return 0, 0, 0


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
fish = []
baby = [0, 0]
length = 0
for i in range(n):
    for j in range(n):
        if board[i][j] and board[i][j] != 9:
            fish.append((board[i][j], i, j))
            length += 1
        elif board[i][j] == 9:
            baby = [i, j]
            board[i][j] = 0
fish.sort(reverse=True)

size = 2
eat = 0
time = 0
goal = []
lg = 0
while True:
    for i in range(length - 1, -1, -1):
        if fish[i][0] < size:
            tmp, fr, fc = fish.pop()
            goal.append((fr, fc))
            lg += 1
            length -= 1
        else:
            break

    baby[0], baby[1], plus = bfs(baby, lg)
    if not plus:
        break
    else:
        board[baby[0]][baby[1]] = 0
        time += plus
        lg -= 1
        eat += 1
        if eat == size:
            size += 1
            eat = 0

print(time)


# 다른 답
n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
size = 2
sizeDic = {i:0 for i in range(1,7)}
current = []
for y in range(n):
    for x in range(n):
        if space[y][x] == 0:
            continue
        elif space[y][x] == 9:
            current = [y, x]
            continue
        sizeDic[space[y][x]] += 1
dy = [0,0,1,-1]
dx = [1,-1,0,0]
def bfs(y, x):
    check = [[False] * n for _ in range(n)]
    check[y][x] = True
    queue = [[0, y, x]]
    result = []
    while not result:
        new_queue = []
        for s, y, x in queue:
            if 0 < space[y][x] < size:
                result.append([s, y, x])
                continue
            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]
                if 0 <= ny < n and 0 <= nx < n and not check[ny][nx]:
                    if space[ny][nx] <= size:
                        new_queue.append([s + 1, ny, nx])
                        check[ny][nx] = True
        queue = new_queue
        if not queue:
            break
    result.sort()
    return result

def findFish():
    step = int(1e9)
    ry, rx = 0, 0
    update = False
    fishes = bfs(current[0], current[1])
    if not fishes:
        return False
    return fishes[0]
time = 0
eat = 0
result = findFish()
while result:
    space[current[0]][current[1]] = 0
    eat += 1
    if eat == size:
        size += 1
        eat = 0
    step, y, x = result
    current = [y, x]
    time += step
    space[y][x] = 0
    result = findFish()

print(time)

