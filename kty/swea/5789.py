import sys

sys.stdin = open("input_5789.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, Q = list(map(int, input().split()))
    K = [list(map(int, input().split())) for _ in range(Q)]
    box = [0] * (N + 1)

    for j in range(len(K)):
        a = K[j]
        for i in range(a[0], a[1] + 1):
            box[i] = j + 1

    print(f'#{tc}', end=' ')
    for i in range(1, len(box)):
        print(str(box[i]), end=' ')
    print()