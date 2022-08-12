T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red = set()
    blue = set()
    for _ in range(N):
        tmp = list(map(int, input().split()))

        if tmp[-1] == 1:

            for row in range(tmp[0], tmp[2]+1):
                for col in range(tmp[1], tmp[3]+1):
                    red.add((row, col))

        else:
            for row in range(tmp[0], tmp[2]+1):
                for col in range(tmp[1], tmp[3]+1):
                    blue.add((row, col))

    result = red & blue

    print(f'#{tc} {len(result)}')
