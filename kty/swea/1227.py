import sys
from collections import deque

sys.stdin = open("input_1227.txt", "r")

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        # 시작 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간에서 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 벽인 경우 무시
            elif graph[nx][ny] == 1:
                continue
            # 해당 노드를 처음 방문 하는 경우에 1로 만들 어서 벽으로 만듬
            elif graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
            # 다음 이동할 곳이 3이 있다면 미로 탈출 성공
            elif graph[nx][ny] == 3:
                return 1
    return 0 # 큐가 다 비었는데도 3을 못 만나면 fail

def find_start(graph):                      # 시작점 찾기
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 2:
                return row, col
def find_end(graph):                        # 도착점 찾기
    for row in range(n):
        for col in range(n):
            if graph[row][col] == 3:
                return row, col

T = 10
n = 100
for _ in range(1, T + 1):
    tc = int(input())
    graph = [list(map(int, input())) for _ in range(n)]
    # 이동할 네 방향 정의(상, 하, 좌, 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    end_x, end_y = find_end(graph)          # 도착점
    start_x, start_y = find_start(graph)    # 시작점

    print(f'#{tc} {bfs(start_x, start_y)}')