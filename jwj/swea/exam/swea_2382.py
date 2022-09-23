T = int(input())

p_dict = {1: 2, 2: 1, 3: 4, 4: 3}

for test_case in range(1, T+1):
    N, M, K = map(int, input().split())

    bio = []

    for _ in range(K):
        tmp = list(map(int, input().split()))
        bio.append(tmp)

    for cnt in range(M):
        maps = [[[] for _ in range(N)] for _ in range(N)]
        for idx, b in enumerate(bio):
            if not b:
                continue
            # 이동
            if b[3] == 1:
                bio[idx][0] -= 1
            elif b[3] == 2:
                bio[idx][0] += 1
            elif b[3] == 3:
                bio[idx][1] -= 1
            elif b[3] == 4:
                bio[idx][1] += 1

            if b[0] == 0 or b[0] == N - 1 or b[1] == 0 or b[1] == N-1:
                bio[idx][2] //= 2
                bio[idx][3] = p_dict[b[3]]     # 위치 변경

            if b[2] == 0:
                bio[idx] = 0
            else:       # 합치기
                maps[b[0]][b[1]].append([idx, b[2], b[3]])

        for row in maps:
            for col in row:
                if len(col) > 1:
                    # print(col)
                    idx = col[0][0]
                    sumV = col[0][1]
                    maxV = col[0][1]
                    p = col[0][2]

                    for b in col[1:]:
                        sumV += b[1]
                        if maxV < b[1]:
                            maxV = b[1]
                            bio[idx] = 0
                            idx = b[0]
                            p = b[2]
                        else:
                            bio[b[0]] = 0

                    bio[idx][2] = sumV
                    bio[idx][3] = p

    result = 0
    for b in bio:
        if b:
            result += b[2]

    print(f'#{test_case} {result}')
