import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())                         # 셀의 개수 N, 격리 시간 M, 미생물 군집의 개수 K
    pops = [list(map(int, input().split())) for _ in range(K)]
    # print(pops) [[1, 1, 7, 1], [2, 1, 7, 1], [5, 1, 5, 4], [3, 2, 8, 4], [4, 3, 14, 1], [3, 4, 3, 3], [1, 5, 8, 2], [3, 5, 100, 1], [5, 5, 1, 1]]
        # 상(1), 하(2), 좌(3), 우(4)
    maximum = [0] * K

    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while M > 0:
        for i in range(K):
            maximum[i] = pops[i][2]

        for i, pp in enumerate(pops):
            if pp[0] == -1:
                continue
            curR, curC = pp[0], pp[1]                                      # 현재 위치
            direction = pp[3]                                              # 방향
            nr, nc = curR + dr[direction-1], curC + dc[direction-1]        #새로운 위치
            num = pp[2]                                                    # 개체수
            if nr == N-1 or nr == 0 :                                         # 약품 처리된 곳
                if direction == 1:
                    direction = 2
                else:
                    direction = 1
                num = pp[2] // 2
            elif nc == N-1 or nc == 0:  # 약품 처리된 곳
                if direction == 3:
                    direction = 4
                elif direction == 4:
                    direction = 3
                num = pp[2] // 2

            pp[0],pp[1],pp[2],pp[3]= nr, nc, num, direction

            if pp[2] == 0:
                pp[0] = -1
            else:
                for j, lst in enumerate(pops[:i]):
                    if lst[0] == pp[0] and lst[1] == pp[1]:
                        num = lst[2] + pp[2]
                        if maximum[j] < maximum[i]:
                            direction = pp[3]
                        else:
                            direction = lst[3]
                            maximum[i] = maximum[j]

                        pp[2], pp[3] = num, direction
                        lst[0],lst[1] = -1,-1

        M -= 1

    res = 0
    for lst in pops:
        if -1 in lst:
            continue
        else:
           res += lst[2]
    print(f'#{tc} {res}')
