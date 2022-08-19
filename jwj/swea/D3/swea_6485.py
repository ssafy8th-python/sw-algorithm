T = int(input())
for tc in range(1, T+1):
    N = int(input())

    bus = [list(map(int, input().split())) for _ in range(N)]

    P = int(input())

    C_lst = [int(input()) for _ in range(P)]

    result = [0] * P

    for idx, C in enumerate(C_lst):
        for A, B in bus:
            if A <= C <= B:
                result[idx] += 1

    print(f'#{tc} ', end='')
    print(*result)

