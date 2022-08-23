T = int(input())


def position(rw):
    row = 1
    row_idx = 1
    while row <= rw:
        row += row_idx
        row_idx += 1

    row -= row_idx

    return row, row_idx-1


for tc in range(1, T+1):
    x, y = map(int, input().split())

    rwV1, rw1 = position(x)
    rwV2, rw2 = position(y)

    x1, y1 = 1+rw1-(x-rwV1), x-rwV1
    x2, y2 = 1+rw2-(y-rwV2), y-rwV2

    x = x1 + x2
    y = y1 + y2

    result = 1
    for i in range(1, x):
        result += i

    i += 2

    for j in range(y-1):
        result += i
        i += 1

    print(f'#{tc} {result}')

