T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())

    fly_lst = [list(map(int, input().split())) for _ in range(N)]

    xSpreay = [[-1, 1], [1, 1], [-1, -1], [1, -1]]
    pSpreay = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    maxV = 0

    for row in range(N):
        for col in range(N):
            position_x = row
            position_y = col
            sumV = fly_lst[row][col]

            for p in pSpreay:
                tmp_x = position_x + p[0]
                tmp_y = position_y + p[1]
                cnt = 1
                while 0 <= tmp_x < N and 0 <= tmp_y < N and cnt < M:
                    sumV += fly_lst[tmp_x][tmp_y]

                    tmp_x += p[0]
                    tmp_y += p[1]

                    cnt += 1

            if sumV > maxV:
                maxV = sumV

            sumV = fly_lst[row][col]

            for p in xSpreay:
                tmp_x = position_x + p[0]
                tmp_y = position_y + p[1]
                cnt = 1
                while 0 <= tmp_x < N and 0 <= tmp_y < N and cnt < M:
                    sumV += fly_lst[tmp_x][tmp_y]

                    tmp_x += p[0]
                    tmp_y += p[1]

                    cnt += 1

            if sumV > maxV:
                maxV = sumV

    print(f'#{tc} {maxV}')
