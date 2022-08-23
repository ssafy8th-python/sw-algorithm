T = int(input())


def dfs(k, s):
    global minV

    if s >= B:
        if minV > s:
            minV = s
    elif k == N:
        return
    else:
        dfs(k+1, H_lst[k]+s)
        dfs(k+1, s)


for tc in range(1, T+1):

    N, B = map(int, input().split())

    H_lst = list(map(int, input().split()))

    minV = sum(H_lst)

    dfs(0, 0)

    print(f'#{tc} {minV-B}')
