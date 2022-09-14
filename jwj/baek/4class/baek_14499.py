N, M, x, y, K = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

commands = list(map(int, input().split()))

dice = [0] * 6

cur_x = x
cur_y = y


def check(new_x, new_y):
    if 0 <= new_x < N and 0 <= new_y < M:
        return True
    return False


for command in commands:

    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    n_x, n_y = cur_x, cur_y

    if command == 1:
        n_y += 1
        if check(n_x, n_y):
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif command == 2:
        n_y -= 1
        if check(n_x, n_y):
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif command == 3:
        n_x -= 1
        if check(n_x, n_y):
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif command == 4:
        n_x += 1
        if check(n_x, n_y):
            dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

    if check(n_x, n_y):
        cur_x, cur_y = n_x, n_y

        if maps[cur_x][cur_y] == 0:
            maps[cur_x][cur_y] = dice[5]
        else:
            dice[5] = maps[cur_x][cur_y]
            maps[cur_x][cur_y] = 0

        print(dice[0])



