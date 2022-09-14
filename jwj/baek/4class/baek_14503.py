from collections import deque

N, M = map(int, input().split())

x, y, d = map(int, input().split())

maps = [input().split() for _ in range(N)]

q = deque()
q.append((x, y, d))

result = 0

visited = [[0] * M for _ in range(N)]

visited[x][y] = 1

result += 1

while q:
    cur_x, cur_y, dir = q.popleft()

    for _ in range(4):
        new_x, new_y = cur_x, cur_y

        if dir == 0:
            dir = 3
            new_y -= 1
        elif dir == 1:
            dir = 0
            new_x -= 1
        elif dir == 2:
            dir = 1
            new_y += 1
        elif dir == 3:
            dir = 2
            new_x += 1

        if 0 <= new_x < N and 0 <= new_y < M:
            if maps[new_x][new_y] == '0' and not visited[new_x][new_y]:
                visited[new_x][new_y] = 1
                q.append((new_x, new_y, dir))
                result += 1
                break
    else:
        new_x, new_y = cur_x, cur_y

        if dir == 0:
            new_x += 1
        elif dir == 1:
            new_y -= 1
        elif dir == 2:
            new_x -= 1
        elif dir == 3:
            new_y += 1

        if 0 <= new_x < N and 0 <= new_y < M and maps[new_x][new_y] == '0':
            q.append((new_x, new_y, dir))

print(result)
