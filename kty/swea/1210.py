import sys

sys.stdin = open("input_1210.txt", "r")

dx = [-1, 1, 0]
dy = [0, 0, -1]

T = 10
for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder[99][i] == 2:
            x = i

    k = 0
    y = 99
    while y > 0:
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < 100 and 0 <= ny < 100 and ladder[ny][nx]:
            ladder[ny][nx] = 0
            x = nx
            y = ny
            k = 0

        else:
            k = (k + 1) % 3
    print('#{} {}'.format(tc, x))


