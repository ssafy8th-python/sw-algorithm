N = int(input())


def recursive(x, y, N):
    if N == 3:
        arr[x][y] = '*'
        arr[x+1][y-1] = '*'
        arr[x+1][y+1] = '*'

        for i in range(-2, 3):
            arr[x + 2][y + i] = '*'
    else:
        N //= 2
        recursive(x, y, N)
        recursive(x + N, y - N, N)
        recursive(x + N, y + N, N)


arr = [[' '] * (N * 2) for _ in range(N)]

recursive(0, N - 1, N)

for a in arr:
    print(''.join(a))