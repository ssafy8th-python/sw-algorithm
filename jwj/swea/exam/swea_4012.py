T = int(input())


def calc(lst):
    res1 = 0
    lst_len = len(lst)
    for i in range(lst_len):
        for j in range(i+1, lst_len):
            res1 += foods[lst[i]][lst[j]] + foods[lst[j]][lst[i]]

    lst_tmp = set(lst)
    remain_tmp = remain_lst - lst_tmp
    remain_tmp = list(remain_tmp)

    res2 = 0
    for i in range(lst_len):
        for j in range(i+1, lst_len):
            res2 += foods[remain_tmp[i]][remain_tmp[j]] + foods[remain_tmp[j]][remain_tmp[i]]

    return abs(res1 - res2)


def nCr(n, r, s):
    global minV
    if lst[-1] >= 1:
        return
    if r == 0:
        res = calc(lst)

        if minV > res:
            minV = res
    else:
        for i in range(s, n - r + 1):
            lst[r-1] = i
            nCr(n, r-1, i+1)


for test_case in range(1, T+1):
    N = int(input())

    foods = [list(map(int, input().split())) for _ in range(N)]

    lst = [0] * (N // 2)
    remain_lst = set(i for i in range(N))

    minV = 200000

    nCr(N, N//2, 0)

    print(f'#{test_case} {minV}')