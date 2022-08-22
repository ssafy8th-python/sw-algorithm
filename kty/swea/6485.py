import sys

sys.stdin = open("input_6485.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    K = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    station = [int(input()) for _ in range(P)]

    world = [0] * 5001
    for bus in K:
        for i in range(bus[0], bus[1] + 1):
            world[i] += 1

    print(f'#{tc}', end=' ')
    for i in station:
        print(str(world[i]), end=' ')
    print()