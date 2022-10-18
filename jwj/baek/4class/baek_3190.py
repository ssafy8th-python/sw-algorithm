from collections import deque

N = int(input())

K = int(input())

apples = [[0] * (N + 1) for _ in range(N+1)]

snake = deque()
snake_dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake_idx = 0
snake.append((1, 1))

for _ in range(K):
    i, j = map(int, input().split())
    apples[i][j] = 1

L = int(input())

time_sum = 0
result = 0
check = False
for _ in range(L):
    time, dir = input().split()
    time = int(time) - result

    for _ in range(time):
        n_x = snake[-1][0] + snake_dir[snake_idx][0]
        n_y = snake[-1][1] + snake_dir[snake_idx][1]

        if 1 <= n_x <= N and 1 <= n_y <= N:
            result += 1

            # 자신의 몸과 만나면 break
            if (n_x, n_y) in snake:
                check = True
                break

            if apples[n_x][n_y] == 1:
                apples[n_x][n_y] = 0
            else:
                snake.popleft()

            snake.append((n_x, n_y))
        else:
            result += 1
            check = True
            break

    if dir == 'D':
        snake_idx += 1
    else:
        snake_idx -= 1

    time_sum += time
    snake_idx %= 4

    if check:
        break

if not check:
    while 1 <= n_x <= N and 1 <= n_y <= N:
        n_x = snake[-1][0] + snake_dir[snake_idx][0]
        n_y = snake[-1][1] + snake_dir[snake_idx][1]

        result += 1

        # 자신의 몸과 만나면 break
        if (n_x, n_y) in snake:
            check = True
            break

        if apples[n_x][n_y] == 1:
            apples[n_x][n_y] = 0
        else:
            snake.popleft()

        snake.append((n_x, n_y))


print(result)
