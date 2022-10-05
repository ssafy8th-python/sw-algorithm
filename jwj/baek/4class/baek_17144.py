import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if lst[i][0] == -1:
        origin_up = i
        origin_down = i+1
        break

for _ in range(T):
    air_up = [origin_up, 0]
    air_down = [origin_down, 0]
    tmp_lst = [[0] * C for _ in range(R)]
    # 미세먼지 확산
    for i in range(R):
        for j in range(C):
            if lst[i][j] >= 5:
                cnt = 0
                spread = lst[i][j] // 5
                for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    n_x = i + d_x
                    n_y = j + d_y
                    if 0 <= n_x < R and 0 <= n_y < C and lst[n_x][n_y] != -1:
                        cnt += 1
                        tmp_lst[n_x][n_y] += spread
                tmp_lst[i][j] += lst[i][j] - spread * cnt

            else:
                tmp_lst[i][j] += lst[i][j]

    # 공기청정기 방향으로 확산

    previous_num = 0
    # 위 방향
    for d_x, d_y in ((0, 1), (-1, 0), (0, -1), (1, 0)):
        n_x = air_up[0] + d_x
        n_y = air_up[1] + d_y

        while 0 <= n_x < R and 0 <= n_y < C:
            if n_x == origin_up and n_y == 0:
                break
            next_num = tmp_lst[n_x][n_y]
            tmp_lst[n_x][n_y] = previous_num
            previous_num = next_num
            n_x += d_x
            n_y += d_y
        else:
            air_up[0] = n_x - d_x
            air_up[1] = n_y - d_y

    previous_num = 0
    # 아래 방향
    for d_x, d_y in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        n_x = air_down[0] + d_x
        n_y = air_down[1] + d_y

        while 0 <= n_x < R and 0 <= n_y < C:
            if n_x == origin_down and n_y == 0:
                break
            next_num = tmp_lst[n_x][n_y]
            tmp_lst[n_x][n_y] = previous_num
            previous_num = next_num
            n_x += d_x
            n_y += d_y
        else:
            air_down[0] = n_x - d_x
            air_down[1] = n_y - d_y

    lst = tmp_lst[::]

result = 0
for l in lst:
    result += sum(l)

print(result + 2)