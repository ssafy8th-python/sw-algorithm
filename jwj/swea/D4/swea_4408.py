T = int(input())

for tc in range(1, T+1):
    N = int(input())

    room = [list(map(int, input().split())) for _ in range(N)]

    result = [0] * 200

    for a, b in room:
        a = (a - 1) // 2
        b = (b - 1) // 2

        if a > b:
            a, b = b, a

        for i in range(a, b+1):
            result[i] += 1


    maxV = 1
    for i in result:
        if maxV < i:
            maxV = i

    print(f'#{tc} {maxV}')
