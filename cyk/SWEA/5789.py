# 현주의 상자 바꾸기
T = int(input())
for tc in range(1, 1+T):
    N, Q = map(int, input().split())

    lst = [0] * (N + 1)
    test = [list(map(int, input().split())) for _ in range(Q)]
    idx = 1
    for elem in test:
        for i in range(elem[0], elem[1]+1):
            lst[i] = idx
        idx += 1
    print(f'#{tc} ', end='')
    print(*lst[1:])