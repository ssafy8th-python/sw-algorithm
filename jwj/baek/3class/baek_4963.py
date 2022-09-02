def bfs(x, y):
    
    q = [(x, y)]

    while q:
        s_x, s_y = q.pop(0)

        for d_x in range(-1, 2):
            for d_y in range(-1, 2):
                if d_x == 0 and d_y == 0:
                    continue

                n_x = s_x + d_x
                n_y = s_y + d_y

                if 0 <= n_x < h and 0 <= n_y < w and ground[n_x][n_y] == 1:
                    ground[n_x][n_y] = 0
                    q.append((n_x, n_y))

                
while True:

    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    ground = [list(map(int, input().split())) for _ in range(h)]

    result = 0

    for i in range(h):
        for j in range(w):
            if ground[i][j] == 1:
                ground[i][j] = 0
                bfs(i, j)
                result += 1

    print(result)