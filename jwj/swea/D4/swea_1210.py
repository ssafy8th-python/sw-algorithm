for tc in range(10):
    test_case = int(input())

    bars = [list(map(int, input().split())) for _ in range(100)]

    dest = 0

    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    for idx in range(100):
        if bars[-1][idx] == 2:
            dest = idx
            break

    curCol = dest
    curRow = 99

    while curRow != 0:

        for i in range(3):
            newRow = curRow + dr[i]
            newCol = curCol + dc[i]

            if 0 <= newRow < 100 and 0 <= newCol < 100 and bars[newRow][newCol] != 0:
                curRow = newRow
                curCol = newCol
                break

        bars[curRow][curCol] = 0

    print(f'#{test_case} {curCol}')
