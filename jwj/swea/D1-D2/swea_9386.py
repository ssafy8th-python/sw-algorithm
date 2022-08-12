T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = input()

    max_cnt = 0
    cnt = 0
    for num in lst:

        if num == '1':
            cnt += 1
        else:
            if max_cnt < cnt :
                max_cnt = cnt
            cnt = 0

    if max_cnt < cnt :
        max_cnt = cnt

    print(f'#{tc} {max_cnt}')
