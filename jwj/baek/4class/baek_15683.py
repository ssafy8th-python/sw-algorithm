from copy import deepcopy


def cctv_search(r, s, lst):
    global minV

    # 모든 사각지대 검사 종료
    if r == 0:
        if minV > s:
            minV = s
        return

    x = cctv_lst[r-1][0]
    y = cctv_lst[r-1][1]

    for d_lst in cctv_dic[room[x][y]]:
        tmp_lst = deepcopy(lst)
        tmp_s = s
        for d_x, d_y in d_lst:
            n_x, n_y = x + d_x, y + d_y

            while 0 <= n_x < N and 0 <= n_y < M:

                if tmp_lst[n_x][n_y] == 0:
                    tmp_lst[n_x][n_y] = -1
                    tmp_s -= 1
                elif tmp_lst[n_x][n_y] == 6:
                    break

                n_x += d_x
                n_y += d_y

        cctv_search(r-1, tmp_s, tmp_lst)


N, M = map(int, input().split())

cctv_dic = {1: [[(0, 1)], [(0, -1)], [(1, -0)], [(-1, 0)]], 2: [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]
    , 3: [[(-1, 0), (0, 1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]
    , 4: [[(-1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, 1)], [(1, 0), (0, -1), (0, 1)], [(-1, 0), (1, 0), (0, -1)]]
    , 5: [[(1, 0), (-1, 0), (0, 1), (0, -1)]]}

room = [list(map(int, input().split())) for _ in range(N)]

cctv_lst = []

empty = 0

for i in range(N):
    for j in range(M):
        if 1 <= room[i][j] <= 5:
            cctv_lst.append((i, j))

        elif room[i][j] == 0:
            empty += 1

tmp = deepcopy(room)

minV = 100

# 모든 cctv 탐색
cctv_search(len(cctv_lst), empty, tmp)

print(minV)
