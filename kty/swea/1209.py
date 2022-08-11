T = 10
for tc in range(1, T+1):
    TC = input()
    N = 100
    arr = [list(map(int, input().split())) for _ in range(N)]

    maxV = 0 # 총 최대 합
    rc = 0  # 왼쪽 상단 -> 오른쪽 하단 대각선 합
    lc = 0  # 오른쪽 상단 -> 왼쪽 하단 대각선 합
    for i in range(N):
        rc += arr[i][i]
        lc += arr[i][N-1-i]

        rs = 0 # 행의 합
        cs = 0 # 열의 합
        for j in range(N):
            rs += arr[i][j]
            cs += arr[j][i]
        if maxV < rs:
            maxV = rs
        if maxV < cs:
            maxV = cs
    if maxV < rc:
        maxV = rc
    if maxV < lc:
        maxV = lc

    print(f'#{tc} {maxV}')