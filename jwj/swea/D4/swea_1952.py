T = int(input())


def dfs(cnt, sum_v):
    # print(cnt)
    global min_v

    if min_v < sum_v:
        return

    if cnt >= 12:
        min_v = sum_v
    else:
        if days[cnt] * charge[0] < charge[1]:
            dfs(cnt + 1, sum_v + (days[cnt] * charge[0]))
        else:
            dfs(cnt+1, sum_v + charge[1])

        dfs(cnt + 3, sum_v + charge[2])


for tc in range(1, T+1):
    charge = list(map(int, input().split()))

    days = list(map(int, input().split()))

    min_v = charge[-1]

    dfs(0, 0)

    print(f'#{tc} {min_v}')