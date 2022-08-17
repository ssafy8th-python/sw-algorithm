T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    lst = [[0] * N for _ in range(N)]

    # 정가운데에 흰돌 흑돌 배치
    lst[N // 2][N // 2] = 2  # 2는 백돌
    lst[N // 2][N // 2 - 1] = 1  # 1는 흑돌
    lst[N // 2 - 1][N // 2 - 1] = 2  # 2는 백돌
    lst[N // 2 - 1][N // 2] = 1  # 1는 백돌

    # print(lst)

    for _ in range(M):
        row, col, dol = map(int, input().split())  # 돌위치, 돌의 색 입력
        row -= 1  # 시작을 1부터 시작하기 때문에 -1을 해서 index 로 변경
        col -= 1

        lst[row][col] = dol

        # 주변 delta 값으로 확인
        for row_delta in range(-1, 2, 1):  # [-1, 0, 1]
            for col_delta in range(-1, 2, 1):  # [-1, 0, 1]
                if row_delta == 0 and col_delta == 0:   # 자신의 위치일 때는 pass
                    continue

                cnt = 0  # 변경할 개수

                is_true = False     # 변경 가능?
                row_tmp = row + row_delta   # 어느 위치까지 변경 할 것인가?
                col_tmp = col + col_delta

                # 맵의 범위를 넘지 말아야 합니다. 또한 해당 위치에 돌이 있어야 합니다.
                while 0 <= row_tmp < N and 0 <= col_tmp < N and lst[row_tmp][col_tmp] != 0:

                    # 자신과 같은 색의 돌이 있을 때
                    if dol == lst[row_tmp][col_tmp]:
                        is_true = True
                        break

                    cnt += 1
                    row_tmp += row_delta
                    col_tmp += col_delta

                # 이동한 cnt 만큼 돌을 바꿔줌
                if is_true:
                    for _ in range(cnt):
                        row_tmp -= row_delta    # delta 값을 이동한 만큼 반대로 빼주면서 이동한 부분의 돌을 바꿔 줍니다.
                        col_tmp -= col_delta
                        lst[row_tmp][col_tmp] = dol

    white = 0
    black = 0

    for i in lst:
        for dol in i:
            if dol == 1:
                black += 1

            elif dol == 2:
                white += 1

    print(f'#{tc} {black} {white}')
