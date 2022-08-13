T = int(input())

for tc in range(1, T+1):
    N = int(input())

    C_lst = list(map(int, input().split()))

    maxV = 0
    maxCnt = 1
    cnt = 0

    for num in C_lst:
        if num > maxV:
            maxV = num

            cnt += 1

            if cnt > maxCnt:
                maxCnt += 1

        else:
            maxV = num
            cnt = 1

    print(f'#{tc} {maxCnt}')
