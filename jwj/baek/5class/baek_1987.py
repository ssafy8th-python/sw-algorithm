def dfs(start_x, start_y, cnt):
    global maxV

    if maxV < cnt:
        maxV = cnt

    for d_x, d_y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        n_x = start_x + d_x
        n_y = start_y + d_y
        if 0 <= n_x < R and 0 <= n_y < C:
            a_num = ord(alphabets[n_x][n_y]) - 65
            if not alpha[a_num]:
                alpha[a_num] = True
                dfs(n_x, n_y, cnt+1)
                alpha[a_num] = False


R, C = map(int, input().split())

alphabets = [input() for _ in range(R)]

alpha = [False] * 26
alpha[ord(alphabets[0][0]) - 65] = True

maxV = 1

dfs(0, 0, 1)

print(maxV)
