
def dfs(i, j, cnt, dist, n):
    global minV

    if minV < dist:
        return

    if cnt == 0:
        if minV > dist:
            minV = dist
    else:
        for idx in range(1, (n // 2) + 1):
            if not monster[idx][0]:
                monster[idx][0] = 1
                p_x, p_y = monster[idx][1], monster[idx][2]
                sumV = abs(i-p_x) + abs(j-p_y)
                dist += sumV
                dfs(p_x, p_y, cnt - 1, dist, n)
                dist -= sumV
                monster[idx][0] = 0

            if monster[idx][0] and not monster[-idx][0]:
                monster[-idx][0] = 1
                p_x, p_y = monster[-idx][1], monster[-idx][2]
                sumV = abs(i-p_x) + abs(j-p_y)
                dist += sumV
                dfs(p_x, p_y, cnt - 1, dist, n)
                dist -= sumV
                monster[-idx][0] = 0
    

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    x, y = 0, 0

    maps = [list(map(int, input().split())) for _ in range(N)]

    monster = [[] for _ in range(9)]

    monster_cnt = 0

    minV = 100000

    for i in range(N):
        for j in range(N):
            if maps[i][j] != 0:
                monster[maps[i][j]].append(0)
                monster[maps[i][j]].append(i)
                monster[maps[i][j]].append(j)
                monster_cnt += 1

    dfs(x, y, monster_cnt, 0, monster_cnt)

    print(f'#{tc} {minV}')
