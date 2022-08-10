N = int(input())

for tc in range(1, N+1):
    N, M = map(int, input().split())

    picture = [list(map(int, input().split())) for _ in range(N)]

    max_distance = 0
    for row in range(N):
        row_distance = 0

        for col in range(M):
            if picture[row][col] == 1:
                row_distance += 1
            else:
                if max_distance < row_distance:
                    max_distance = row_distance
                    row_distance = 0
        if max_distance < row_distance:
            max_distance = row_distance

    for col in range(M):
        col_distance = 0

        for row in range(N):
            if picture[row][col] == 1:
                col_distance += 1
            else:
                if max_distance < col_distance:
                    max_distance = col_distance
                    col_distance = 0
        if max_distance < col_distance:
            max_distance = col_distance

    print(f'#{tc} {max_distance}')
